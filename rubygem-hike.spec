%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from hike-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hike

Summary: Find files in a set of paths
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.3
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/sstephenson/hike
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sstephenson/hike.git && cd hike && git checkout v1.2.3
# tar czvf hike-1.2.3-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A Ruby library for finding files in a set of paths.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}
%{?scl:scl enable %scl - << \EOF}
# To run the tests using minitest 5
ruby -rminitest/autorun -Ilib:test - << \RUBY
  module Kernel
    alias orig_require require
    remove_method :require

    def require path
      orig_require path unless path == 'test/unit'
    end

  end

  Test = Minitest

  Dir.glob "./test/test_*.rb", &method(:require)
RUBY
%{?scl:EOF}
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}


%changelog
* Mon Jan 26 2015 Josef Stribny <jstribny@redhat.com> - 1.2.3-1
- Update to 1.2.3

* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 1.2.1-5
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Wed Jun 12 2013 Josef Stribny <jstribny@redhat.com> - 1.2.1-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-3
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.1-2
- Rebuilt for scl.

* Mon Jan 30 2012 Vít Ondruch <vondruch@redhat.com> - 1.2.1-1
- Update to Hike 1.2.1.

* Wed Jun 29 2011 Vít Ondruch <vondruch@redhat.com> - 1.1.0-1
- Initial package
