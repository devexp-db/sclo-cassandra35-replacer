Name:          replacer
Version:       1.5.2
Release:       3%{?dist}
Summary:       Replacer Maven Mojo
License:       MIT
URL:           http://code.google.com/p/maven-replacer-plugin/
# svn export http://maven-replacer-plugin.googlecode.com/svn/tags/replacer-1.5.2/trunk/ replacer-1.5.2
# tar czf replacer-1.5.2-src-svn.tar.gz replacer-1.5.2
Source0:       %{name}-%{version}-src-svn.tar.gz
# replacer don't include the license file. see: http://code.google.com/p/maven-replacer-plugin/issues/detail?id=84
BuildRequires: java-devel

BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent)
BuildRequires: mvn(xerces:xercesImpl)

# test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest-all)
BuildRequires: mvn(org.mockito:mockito-all)

BuildRequires: maven-local
BuildRequires: maven-plugin-plugin

BuildArch:     noarch

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_remove_plugin :dashboard-maven-plugin

%mvn_file :%{name} %{name}
%mvn_alias :%{name} com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 1.5.2-2
- switch to XMvn
- minor changes to adapt to current guideline

* Sun May 26 2013 gil cattaneo <puntogil@libero.it> 1.5.2-1
- initial rpm