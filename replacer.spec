Name:          replacer
Version:       1.5.2
Release:       1%{?dist}
Summary:       Replacer Maven Mojo
Group:         Development/Libraries
License:       MIT
URL:           http://code.google.com/p/maven-replacer-plugin/
# svn export http://maven-replacer-plugin.googlecode.com/svn/tags/replacer-1.5.2/trunk/ replacer-1.5.2
# tar czf replacer-1.5.2-src-svn.tar.gz replacer-1.5.2
Source0:       %{name}-%{version}-src-svn.tar.gz
# replacer don't include the license file. see: http://code.google.com/p/maven-replacer-plugin/issues/detail?id=84
BuildRequires: java-devel

BuildRequires: ant
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: xerces-j2

# test deps
BuildRequires: junit
BuildRequires: mockito
BuildRequires: hamcrest12
# mvn(org.hamcrest:hamcrest-all) = 1.1

BuildRequires: maven-local
BuildRequires: maven-plugin-plugin

Requires:      ant
Requires:      apache-commons-io
Requires:      apache-commons-lang
Requires:      mvn(org.apache.maven:maven-plugin-api)
Requires:      xerces-j2

Requires:      java
BuildArch:     noarch

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Group:         Documentation
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_remove_plugin :dashboard-maven-plugin

%build
# required hamcrest 1.1 and 1.3 isnt available in F18
mvn-rpmbuild \
  -Dmaven.local.depmap.file="%{_mavendepmapfragdir}/hamcrest12" \
  package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a "com.google.code.maven-replacer-plugin:maven-replacer-plugin"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun May 26 2013 gil cattaneo <puntogil@libero.it> 1.5.2-1
- initial rpm