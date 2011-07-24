# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define     short_name      logkit
%define     camelcase_short_name      LogKit

Name:        avalon-%{short_name}
Version:     1.2
Release:     8.2%{?dist}
Epoch:       0
Summary:     Java logging toolkit
License:     ASL 1.1
Group:       Development/Libraries/Java
URL:         http://avalon.apache.org/%{short_name}/
Source0:     http://archive.apache.org/dist/avalon/logkit/LogKit-1.2-src.tar.gz
Patch0:      %{name}-build.patch
Patch1:      %{name}-javadoc.patch
Patch2:      %{name}-notarget.patch
Requires:    avalon-framework >= 0:4.1.4
Requires:    servlet
Requires:    jms
Requires:    jdbc-stdext
BuildRequires:    jpackage-utils >= 0:1.5
BuildRequires:    ant
BuildRequires:    javamail
BuildRequires:    junit
BuildRequires:    log4j
BuildRequires:    avalon-framework >= 0:4.1.4
BuildRequires:    servlet
BuildRequires:    jms
BuildRequires:    jdbc-stdext
BuildArch:    noarch
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
LogKit is a logging toolkit designed for secure performance orientated
logging in applications. To get started using LogKit, it is recomended
that you read the whitepaper and browse the API docs.

%package javadoc
Summary:    Javadoc for %{name}
Group:        Development/Documentation
Requires(post):   /bin/rm,/bin/ln
Requires(postun): /bin/rm

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{camelcase_short_name}-%{version}

%patch0
%patch1 -p1
%patch2 -p1

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
export CLASSPATH=%(build-classpath log4j javamail/mailapi jms servlet jdbc-stdext avalon-framework junit):$PWD/build/classes
ant clean jar javadocs

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc KEYS LICENSE
%{_javadir}/*

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}

%changelog
* Mon Feb 22 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-8.2
- Drop gcj_support
- Fix Source0 url.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0:1.2-8.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.2-6
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.2-5jpp.5
- Autorebuild for GCC 4.3

* Fri Feb 09 2007 Permaine Cheung <pcheung@redhat.com> 0:1.2-4jpp.5%{?dist}
- Fix source URL, BuildRoot

* Thu Feb 08 2007 Permaine Cheung <pcheung@redhat.com> 0:1.2-4jpp.4%{?dist}
- rpmlint cleanup.

* Thu Aug 03 2006 Deepak Bhole <dbhole@redhat.com> 0:1.2-4jpp.3
- Added missing requirements.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.2-4jpp_2fc
- Rebuilt

* Wed Jul 19 2006 Deepak Bhole <dbhole@redhat.com> 0:1.2-4jpp_1fc
- Added conditional native compilation.
- Removed name/release/version defines as applicable.

* Fri Aug 20 2004 Ralph Apel <r.apel@r-apel.de> 0:1.2-3jpp
- Build with ant-1.6.2

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:1.2-2jpp
- update for JPackage 1.5

* Fri Mar 21 2003 Nicolas Mailhot <Nicolas.Mailhot (at) JPackage.org> 1.2-1jpp
- For jpackage-utils 1.5

* Tue May 07 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0.1-4jpp 
- hardcoded distribution and vendor tag
- group tag again

* Thu May 2 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0.1-3jpp 
- distribution tag
- group tag

* Mon Mar 18 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0.1-2jpp 
- generic servlet support

* Sun Feb 03 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0.1-1jpp 
- 1.0.1
- versioned dir for javadoc
- no dependencies for and javadoc package
- adaptation for new servlet3 package
- drop j2ee package
- regenerated the patch
- section package

* Wed Dec 5 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-4jpp
- javadoc into javadoc package
- Requires and BuildRequires servletapi3 >= 3.2.3-2
- regenerated the patch

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 1.0-3jpp
- changed extension --> jpp

* Tue Nov 20 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-2jpp
- non-free extension classes back in original archive
- removed packager tag

* Sun Oct 28 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-1jpp
- 1.0

* Tue Oct 9 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b5.2jpp
- non-free extension as additional package

* Sat Oct 6 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b5.1jpp
- 1.0b5
- first unified release
- used original tarball

* Mon Sep 10 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b4.1mdk
- first Mandrake release
