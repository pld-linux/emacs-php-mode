%define		_orig_name	php-mode
%define		_emacs_version	21.2
%define		_php_mode_ver	1.0.2
#%define		_pack_ver	%(echo %{_php_mode_ver} | sed -e "s/\.//g")

Summary:	The Emacs php-mode text editor for the X Window System
Summary(de.UTF-8):   GNU Emacs php-mode
Summary(es.UTF-8):   GNU Emacs php-mode
Summary(fr.UTF-8):   GNU Emacs php-mode
Summary(pl.UTF-8):   GNU Emacs php-mode - Narzędzia pomocnicze do PHP
Summary(pt_BR.UTF-8):   GNU Emacs php-mode
Summary(tr.UTF-8):   GNU Emacs php-mode
Name:		emacs-el-%{_orig_name}
Version:	%{_php_mode_ver}
Release:	1
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://dl.sourceforge.net/php-mode/%{_orig_name}-102.el
# Source0-md5:	bbf006aec2f76f8bb609d4314df3a065
URL:		http://php-mode.sourceforge.net/
Requires:	emacs-el = %{_emacs_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
php-mode - An Emacs major mode for editing PHP code. Features:
  - Syntax coloring and indenting;
  - Documentation browse and search functions;
  - Support for Imenu and SpeedBar;
  - Customization options.

%description -l pl.UTF-8
php-mode - rozszerzenie do Emacsa ułatwiające edycję plików php.
Zalety:
  - kolorowanie składni i indeksowanie;
  - Przeglądanie dokumentów i szukanie funkcji;
  - Wsparcie dla Imenu oraz SpeedBar;
  - Opcje dostosowania do własnych potrzeb.

%prep
%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/%{_emacs_version}/lisp/progmodes/
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/emacs/%{_emacs_version}/lisp/progmodes/%{_orig_name}.el

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/emacs/%{_emacs_version}/lisp/progmodes/%{_orig_name}.el
