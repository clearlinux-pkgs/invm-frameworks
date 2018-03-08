#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : invm-frameworks
Version  : 01.01.00.2103
Release  : 4
URL      : https://github.com/intel/invm-frameworks/archive/v01.01.00.2103.tar.gz
Source0  : https://github.com/intel/invm-frameworks/archive/v01.01.00.2103.tar.gz
Summary  : Framework for Storage I18N, CLI and CIM applications
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear BSL-1.0
Requires: invm-frameworks-lib
BuildRequires : cmake

%description
Framework library supporting a subset of Internationalization (I18N)
functionality, storage command line interface (CLI) applications, storage
common information model (CIM) providers.

%package dev
Summary: dev components for the invm-frameworks package.
Group: Development
Requires: invm-frameworks-lib
Provides: invm-frameworks-devel

%description dev
dev components for the invm-frameworks package.


%package lib
Summary: lib components for the invm-frameworks package.
Group: Libraries

%description lib
lib components for the invm-frameworks package.


%prep
%setup -q -n invm-frameworks-01.01.00.2103

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520549290
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_INSTALL_LIBDIR:PATH=lib64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1520549290
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## make_install_append content
mkdir -p %{buildroot}/usr/include/libinvm-cim/cmpi
cp -a external/invm-cim/cmpi/include/cmpi/*.h %{buildroot}/usr/include/libinvm-cim/cmpi/
## make_install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libinvm-cim/AssociationFactory.h
/usr/include/libinvm-cim/AssociationMapper.h
/usr/include/libinvm-cim/Attribute.h
/usr/include/libinvm-cim/CimXml.h
/usr/include/libinvm-cim/CimomAdapter.h
/usr/include/libinvm-cim/CmpiAdapter.h
/usr/include/libinvm-cim/Exception.h
/usr/include/libinvm-cim/ExceptionBadAttribute.h
/usr/include/libinvm-cim/ExceptionBadParameter.h
/usr/include/libinvm-cim/ExceptionInvalidWqlQuery.h
/usr/include/libinvm-cim/ExceptionNoMemory.h
/usr/include/libinvm-cim/ExceptionNotSupported.h
/usr/include/libinvm-cim/ExceptionSystemError.h
/usr/include/libinvm-cim/Export.h
/usr/include/libinvm-cim/IndicationService.h
/usr/include/libinvm-cim/Instance.h
/usr/include/libinvm-cim/InstanceFactory.h
/usr/include/libinvm-cim/InstanceFactoryCreator.h
/usr/include/libinvm-cim/IntelCmpiProvider.h
/usr/include/libinvm-cim/IntelToCmpi.h
/usr/include/libinvm-cim/Logger.h
/usr/include/libinvm-cim/NullInstanceFactory.h
/usr/include/libinvm-cim/ObjectPath.h
/usr/include/libinvm-cim/ObjectPathBuilder.h
/usr/include/libinvm-cim/ProviderFactory.h
/usr/include/libinvm-cim/StringUtil.h
/usr/include/libinvm-cim/Strings.h
/usr/include/libinvm-cim/Trace.h
/usr/include/libinvm-cim/Types.h
/usr/include/libinvm-cim/WqlConditional.h
/usr/include/libinvm-cim/WqlQuery.h
/usr/include/libinvm-cim/cmpi/cmpidt.h
/usr/include/libinvm-cim/cmpi/cmpift.h
/usr/include/libinvm-cim/cmpi/cmpimacs.h
/usr/include/libinvm-cim/cmpi/cmpios.h
/usr/include/libinvm-cim/cmpi/cmpipl.h
/usr/include/libinvm-cim/common_types.h
/usr/include/libinvm-cim/logging.h
/usr/include/libinvm-cim/revision.h
/usr/include/libinvm-cim/s_str.h
/usr/include/libinvm-cim/time_utilities.h
/usr/include/libinvm-cim/unicode_utilities.h
/usr/include/libinvm-cim/x_str.h
/usr/include/libinvm-cli/CliFrameworkTypes.h
/usr/include/libinvm-cli/CommandFilter.h
/usr/include/libinvm-cli/CommandSpec.h
/usr/include/libinvm-cli/CommandVerify.h
/usr/include/libinvm-cli/DuplicateTokenErrorResult.h
/usr/include/libinvm-cli/ErrorResult.h
/usr/include/libinvm-cli/Export.h
/usr/include/libinvm-cli/FeatureBase.h
/usr/include/libinvm-cli/FeatureRef.h
/usr/include/libinvm-cli/Framework.h
/usr/include/libinvm-cli/HelpFeature.h
/usr/include/libinvm-cli/HelpResult.h
/usr/include/libinvm-cli/Lexer.h
/usr/include/libinvm-cli/Logger.h
/usr/include/libinvm-cli/NoInputErrorResult.h
/usr/include/libinvm-cli/NotImplementedErrorResult.h
/usr/include/libinvm-cli/ObjectListResult.h
/usr/include/libinvm-cli/OutputOptions.h
/usr/include/libinvm-cli/OutputOptionsValidator.h
/usr/include/libinvm-cli/ParseErrorResult.h
/usr/include/libinvm-cli/Parser.h
/usr/include/libinvm-cli/PropertyListResult.h
/usr/include/libinvm-cli/ResultBase.h
/usr/include/libinvm-cli/SimpleListResult.h
/usr/include/libinvm-cli/SimpleResult.h
/usr/include/libinvm-cli/SyntaxErrorBadValueResult.h
/usr/include/libinvm-cli/SyntaxErrorMissingValueResult.h
/usr/include/libinvm-cli/SyntaxErrorResult.h
/usr/include/libinvm-cli/SyntaxErrorUnexpectedValueResult.h
/usr/include/libinvm-cli/Trace.h
/usr/include/libinvm-cli/cr_i18n.h
/usr/include/libinvm-cli/osAdapter.h
/usr/include/libinvm-i18n/libIntel_i18n.h
/usr/lib64/libinvm-cim.so
/usr/lib64/libinvm-cli.so
/usr/lib64/libinvm-i18n.so
/usr/lib64/pkgconfig/libinvm-cim.pc
/usr/lib64/pkgconfig/libinvm-cli.pc
/usr/lib64/pkgconfig/libinvm-i18n.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libinvm-cim.so.2
/usr/lib64/libinvm-cim.so.2.0.0
/usr/lib64/libinvm-cli.so.2
/usr/lib64/libinvm-cli.so.2.0.0
/usr/lib64/libinvm-i18n.so.2
/usr/lib64/libinvm-i18n.so.2.0.0
