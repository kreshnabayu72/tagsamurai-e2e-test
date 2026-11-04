---
id: TC-FA-LBL-E2E-059-role-matrix-visibilitas-tab-labels-read-only-manage-asset-master-data-dan-role-lain
title: "Role Matrix: visibilitas elemen tab Labels: Read Only, Manage Asset Master Data (Create, Update, Delete independen), dan Role Lain"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:ui-visibility-per-role-capability/read-only
  - FALB:ui-visibility-per-role-capability/manage-asset-master-data-permission-create-updat
  - FALB:ui-visibility-per-role-capability/role-lain-tanpa-capability
  - FALB:component-states/disabled-vs-hidden
coverage:
  web: automated
---

# Role Matrix: visibilitas elemen tab Labels: Read Only, Manage Asset Master Data (Create, Update, Delete independen), dan Role Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Read Only (`DU-02`), env `FA_RO_EMAIL` dan `FA_RO_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (`DU-01`, env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`).
- Role yang diuji (akun hanya lewat env, tidak ada password di spec); kolom hasil mengikuti matriks PRD §2.1:

| Role | Data | Env email | Env password | Tab Labels | Create | Edit | Delete | Download | View Tagged Assets |
|---|---|---|---|---|---|---|---|---|---|
| Read Only | `DU-02` | `FA_RO_EMAIL` | `FA_RO_PASSWORD` | tampil | Hidden | Hidden | Hidden | tampil | tampil |
| Create Only (Permission Create pada "Manage Asset Master Data") | `DU-03` | `FA_CO_EMAIL` | `FA_CO_PASSWORD` | tampil | tampil | Hidden | Hidden | tampil | tampil |
| Update Only (Permission Update pada "Manage Asset Master Data") | `DU-04` | `FA_UO_EMAIL` | `FA_UO_PASSWORD` | tampil | Hidden | tampil | Hidden | tampil | tampil |
| Delete Only (Permission Delete pada "Manage Asset Master Data") | `DU-05` | `FA_DO_EMAIL` | `FA_DO_PASSWORD` | tampil | Hidden | Hidden | tampil | tampil | tampil |
| Role Lain tanpa capability | `DU-06` | `FA_NOROLE_EMAIL` | `FA_NOROLE_PASSWORD` | Hidden | tidak terjangkau | tidak terjangkau | tidak terjangkau | tidak terjangkau | tidak terjangkau |

- Data uji: `DU-18` (label seed milik spec, bersuffix `{runId}-059`, warna `#3B82F6`, dibuat lewat API di hook `before` dan dihapus di hook `after`) sebagai baris target untuk menu `[⋯]`.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, disediakan tim FE/BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:ui-visibility-per-role-capability/read-only: Read Only

1. Ketik Search `DU-18`, tekan Enter
2. Verifikasi tab `Labels` aktif dan baris label `DU-18` tampil pada Labels List
3. Verifikasi tombol Download dan ikon Changelog tampil pada toolbar tabel
4. Verifikasi tombol `[+ Label]` tidak tampil pada toolbar tabel
5. Klik `[⋯]` pada baris label `DU-18`
6. Verifikasi aksi `Detail` tampil pada menu `[⋯]`
7. Verifikasi aksi `Edit` dan `Delete` tidak tampil pada menu `[⋯]`

### FALB:component-states/disabled-vs-hidden: Elemen yang dibatasi otorisasi role disembunyikan (Hidden), bukan Disabled

8. Verifikasi tombol `[+ Label]` tidak ada pada toolbar tabel, bukan tampil dengan state Disabled
9. Verifikasi menu `[⋯]` tidak memuat `Edit` dan `Delete` sebagai item Disabled

### FALB:ui-visibility-per-role-capability/manage-asset-master-data-permission-create-updat: "Manage Asset Master Data": Permission Create, Update, dan Delete masing-masing independen

10. Ganti akun ke Create Only: logout, login dengan akun `DU-03`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
11. Ketik Search `DU-18`, tekan Enter
12. Verifikasi tab `Labels` aktif dan baris label `DU-18` tampil pada Labels List
13. Verifikasi tombol Download dan ikon Changelog tampil pada toolbar tabel
14. Verifikasi tombol `[+ Label]` tampil pada toolbar tabel
15. Klik `[⋯]` pada baris label `DU-18`
16. Verifikasi aksi `Detail` tampil pada menu `[⋯]`
17. Verifikasi aksi `Edit` dan `Delete` tidak tampil pada menu `[⋯]`
18. Ganti akun ke Update Only: logout, login dengan akun `DU-04`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
19. Ketik Search `DU-18`, tekan Enter
20. Verifikasi tab `Labels` aktif dan baris label `DU-18` tampil pada Labels List
21. Verifikasi tombol Download dan ikon Changelog tampil pada toolbar tabel
22. Verifikasi tombol `[+ Label]` tidak tampil pada toolbar tabel
23. Klik `[⋯]` pada baris label `DU-18`
24. Verifikasi aksi `Detail` dan `Edit` tampil pada menu `[⋯]`
25. Verifikasi aksi `Delete` tidak tampil pada menu `[⋯]`
26. Ganti akun ke Delete Only: logout, login dengan akun `DU-05`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
27. Ketik Search `DU-18`, tekan Enter
28. Verifikasi tab `Labels` aktif dan baris label `DU-18` tampil pada Labels List
29. Verifikasi tombol Download dan ikon Changelog tampil pada toolbar tabel
30. Verifikasi tombol `[+ Label]` tidak tampil pada toolbar tabel
31. Klik `[⋯]` pada baris label `DU-18`
32. Verifikasi aksi `Detail` dan `Delete` tampil pada menu `[⋯]`
33. Verifikasi aksi `Edit` tidak tampil pada menu `[⋯]`

### FALB:ui-visibility-per-role-capability/role-lain-tanpa-capability: Role Lain tanpa capability

34. Ganti akun ke Role Lain tanpa capability: logout, login dengan akun `DU-06`, lalu buka Fixed Asset > Settings > Asset Master
35. Verifikasi halaman Settings > Asset Master termuat
36. Verifikasi tab `Labels` tidak tampil pada daftar tab

## Notes

- Langkah penghubung (S-03): Search `DU-18` (langkah 1, 11, 19, 27) menemukan baris target di Labels List yang dapat memuat lebih dari satu halaman (R-16); klik `[⋯]` (langkah 5, 15, 23, 31) membuka menu baris; langkah ganti akun (10, 18, 26, 34) berupa langkah eksplisit tanpa `Verifikasi` karena akun pertama login di hook `before`.
- Spec ditulis per blok role dengan ganti akun eksplisit (konvensi bagian 3a): pola langkah tiap role sama, hasil per role berbeda, dan Read Only login di hook `before`.
- Anchor absence: baris label `DU-18` tampil (langkah 2, 12, 20, 28) serta tombol Download dan ikon Changelog tampil (langkah 3, 13, 21, 29; PRD §2.1 Download Export dan §3.7 Download dan Changelog "Selalu berlaku") mendahului asersi Hidden untuk `[+ Label]`; aksi `Detail` tampil (langkah 6, 16, 24, 32; PRD §2.1 View Tagged Assets dan §4.7) mendahului asersi `Edit` dan `Delete` tidak tampil; `Edit` tampil (langkah 24) dan `Delete` tampil (langkah 32) menjadi anchor untuk asersi pasangannya; halaman Settings > Asset Master yang termuat (langkah 35) mendahului asersi tab `Labels` tidak tampil.
- Pembagian klausa lintas spec: `FALB:component-states/disabled-vs-hidden` dikutip spec 037, 058, dan 059; spec ini mengasersi bahwa `[+ Label]`, `Edit`, dan `Delete` bagi Read Only Hidden dan bukan Disabled (langkah 8 dan 9), spec 058 mengasersi tab `Labels` Hidden bagi Group Manager tanpa capability, dan spec 037 mengasersi Submit Disabled pada form.
- Temuan PRD: matriks §2.1 dan §4.7 tidak ber-ID per sel sehingga tiap kombinasi role × aksi tidak dapat dikutip sebagai aturan sendiri; Download Export dan View Tagged Assets dipakai hanya sebagai anchor (langkah 3, 6, 13, 16, 21, 24, 29, dan 32), dan visibilitas kolom checkbox serta Bulk Action Bar (§4.7) diasersi di spec 060.
- Temuan PRD: PRD tidak menyatakan apa yang tampil bila Role Lain membuka Settings > Asset Master dan tidak menyatakan elemen yang pasti tampil di halaman itu (tab `Asset Name` juga dinaungi "Manage Asset Master Data"), sehingga asersi tab `Labels` tidak tampil (langkah 36) hanya beranchor halaman yang termuat.
- Alasan spec melewati 35 langkah: lima blok role satu kelas harness (Role Matrix) dengan pola langkah yang sama dan tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan pemecahan menambah login dan seeding `DU-18` per spec.
