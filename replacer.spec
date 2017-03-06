%{?scl:%scl_package replacer}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}replacer
Version:	1.6
Release:	5%{?dist}
Summary:	Replacer Maven Mojo
License:	MIT
URL:		https://github.com/beiliubei/maven-replacer-plugin
# http://code.google.com/p/maven-replacer-plugin/
Source0:	https://github.com/beiliubei/maven-replacer-plugin/archive/%{version}.tar.gz

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_java_common}apache-commons-io
BuildRequires:	%{?scl_prefix_java_common}apache-commons-lang
BuildRequires:	%{?scl_prefix_java_common}junit
BuildRequires:	%{?scl_prefix_java_common}ant
BuildRequires:	%{?scl_prefix_maven}maven
BuildRequires:	%{?scl_prefix_maven}maven-plugin-plugin
BuildRequires:	%{?scl_prefix_java_common}hamcrest
BuildRequires:	%{?scl_prefix_maven}mockito
BuildRequires:	%{?scl_prefix_maven}sonatype-oss-parent
BuildRequires:	%{?scl_prefix_java_common}xerces-j2
BuildRequires:	%{?scl_prefix_java_common}xml-commons-apis
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n maven-replacer-plugin-%{version}

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
# NoClassDefFoundError: org/w3c/dom/ElementTraversal
%pom_add_dep xml-apis:xml-apis::test

sed -i.hamcrest '/startsWith/d' src/test/java/com/google/code/maven_replacer_plugin/file/FileUtilsTest.java

%mvn_file :%{pkg_name} %{pkg_name}
%mvn_alias :%{pkg_name} com.google.code.maven-replacer-plugin:maven-replacer-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon Mar 06 2017 Tomas Repik <trepik@redhat.com> - 1.6-5
- scl conversion

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 gil cattaneo <puntogil@libero.it> 1.6-1
- update to 1.6
- fix Url tag and Source0 tag

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.5.3-2
- introduce license macro

* Thu Jul 03 2014 gil cattaneo <puntogil@libero.it> 1.5.3-1
- update to 1.5.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.5.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 1.5.2-2
- switch to XMvn
- minor changes to adapt to current guideline

* Sun May 26 2013 gil cattaneo <puntogil@libero.it> 1.5.2-1
- initial rpm
