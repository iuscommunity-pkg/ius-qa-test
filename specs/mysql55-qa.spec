Name:       mysql55-qa		
Version:    1.0	
Release:	1%{?dist}
Summary:	IUS QA Test Spec

Group:	    Development/Tools	
License:	GPL
URL:		http://iuscommunity.org
Source0:	README
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	mysql55 mysql55-server mysql55-libs mysql55-embedded 
BuildRequires:  mysql55-devel mysql55-bench mysql55-test

Requires:	mysql55 mysql55-server mysql55-libs mysql55-embedded 
Requires:   mysql55-devel mysql55-bench mysql55-test

%description
IUS QA Test Spec for %{name}.

%prep
%setup -q


%build
# pass

%install
rm -rf $RPM_BUILD_ROOT
# pass

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README



%changelog
* Thu Feb 11 2011 BJ Dierkes <wdierkes@rackspace.com> - 1.0-1
- Initial spec
