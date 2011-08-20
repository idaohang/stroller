# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# >> macros
%if X%{_vendor} == "Xmeego"
%define my_buildhost "meego"
%else
%define my_exec_dir "/usr/bin"
%if X%{_vendor} == "Xredhat"
%define qmake qmake-qt4 \
make
%else
%define qmake qmake \
make
%endif
%define qmake_install mkdir -p %{buildroot}%{my_exec_dir} && \
make INSTALL_ROOT=%{buildroot} install
%define my_buildhost non-meego-%{vendor}
%endif
# << macros

# << macros

Name:       stroller
Summary:    A GPS Tracker
Version:    0.0.2
Release:    1
Group:      Applications/Productivity
License:    GPLv2+
URL:        https://github.com/berndhs/stroller
Source0:    stroller-%{version}.tar.gz
Source100:  stroller.yaml
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(QtMobility)


%description
A simple GPS tracker showing where the user/device has been 




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
# >> files
# << files

