---
id: TC-FA-LBL-E2E-058-role-matrix-visibilitas-tab-labels-total-control-default-user-dan-group-manager
title: "Role Matrix: visibilitas elemen tab Labels: Total Control, Default User, dan Group Manager"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:ui-visibility-per-role-capability/total-control
  - FALB:ui-visibility-per-role-capability/default-user
  - FALB:ui-visibility-per-role-capability/group-manager-tier-per-user-group
  - FALB:component-states/disabled-vs-hidden
coverage:
  web: automated
---

# Role Matrix: visibilitas elemen tab Labels: Total Control, Default User, dan Group Manager

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke `DU-01`.
- Role yang diuji (akun hanya lewat env, tidak ada password di spec); kolom hasil mengikuti matriks PRD §2.1:

| Role | Data | Env email | Env password | Tab Labels | Create | Edit | Delete | Download | View Tagged Assets |
|---|---|---|---|---|---|---|---|---|---|
| Total Control | `DU-01` | `FA_TC_EMAIL` | `FA_TC_PASSWORD` | tampil | tampil | tampil | tampil | tampil | tampil |
| Default User | `DU-63` | `FA_DU_EMAIL` | `FA_DU_PASSWORD` | tampil | tampil | tampil | tampil | tampil | tampil |
| Group Manager tanpa capability "Manage Asset Master Data" | `DU-64` | `FA_GMNOCAP_EMAIL` | `FA_GMNOCAP_PASSWORD` | Hidden | tidak terjangkau | tidak terjangkau | tidak terjangkau | tidak terjangkau | tidak terjangkau |
| Group Manager dengan capability "Manage Asset Master Data" (Permission Create, Update, Delete) | `DU-65` | `FA_GMCRUD_EMAIL` | `FA_GMCRUD_PASSWORD` | tampil | tampil | tampil | tampil | tampil | tampil |

- Data uji: `DU-18` (label seed milik spec, bersuffix `{runId}-058`, warna `#3B82F6`, dibuat lewat API di hook `before` dan dihapus di hook `after`) sebagai baris target untuk menu `[⋯]`.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, disediakan tim FE/BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:ui-visibility-per-role-capability/total-control: Total Control

1. Ketik Search `DU-18`, tekan Enter
2. Verifikasi tab `Labels` aktif dan baris label `DU-18` tampil pada Labels List
3. Verifikasi tombol `[+ Label]` tampil pada toolbar tabel
4. Verifikasi tombol Download tampil pada toolbar tabel
5. Klik `[⋯]` pada baris label `DU-18`
6. Verifikasi aksi `Detail`, `Edit`, dan `Delete` tampil pada menu `[⋯]`

### FALB:ui-visibility-per-role-capability/default-user: Default User

7. Ganti akun ke Default User: logout, login dengan akun `DU-63`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
8. Ketik Search `DU-18`, tekan Enter
9. Verifikasi tab `Labels` aktif dan baris label `DU-18` tampil pada Labels List
10. Verifikasi tombol `[+ Label]` tampil pada toolbar tabel
11. Verifikasi tombol Download tampil pada toolbar tabel
12. Klik `[⋯]` pada baris label `DU-18`
13. Verifikasi aksi `Detail`, `Edit`, dan `Delete` tampil pada menu `[⋯]`

### FALB:component-states/disabled-vs-hidden: Elemen yang dibatasi otorisasi role disembunyikan (Hidden), bukan Disabled

14. Ganti akun ke Group Manager tanpa capability: logout, login dengan akun `DU-64`, lalu buka Fixed Asset > Settings > Asset Master
15. Verifikasi halaman Settings > Asset Master termuat
16. Verifikasi tab `Labels` tidak tampil pada daftar tab, bukan tampil dengan state Disabled

### FALB:ui-visibility-per-role-capability/group-manager-tier-per-user-group: Group Manager: akses ditentukan capability "Manage Asset Master Data", bukan tier Group Manager

17. Ganti akun ke Group Manager dengan capability: logout, login dengan akun `DU-65`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
18. Ketik Search `DU-18`, tekan Enter
19. Verifikasi tab `Labels` aktif dan baris label `DU-18` tampil pada Labels List
20. Verifikasi tombol `[+ Label]` tampil pada toolbar tabel
21. Verifikasi tombol Download tampil pada toolbar tabel
22. Klik `[⋯]` pada baris label `DU-18`
23. Verifikasi aksi `Detail`, `Edit`, dan `Delete` tampil pada menu `[⋯]`

## Notes

- Langkah penghubung (S-03): Search `DU-18` (langkah 1, 8, 18) menemukan baris target di Labels List yang dapat memuat lebih dari satu halaman (R-16); klik `[⋯]` (langkah 5, 12, 22) membuka menu baris; langkah ganti akun (7, 14, 17) berupa langkah eksplisit tanpa `Verifikasi` karena akun pertama login di hook `before`.
- Spec ditulis per blok role dengan ganti akun eksplisit (konvensi bagian 3a): pola langkah tiap role sama, hasil per role berbeda, dan Total Control login di hook `before`.
- Anchor absence: langkah 15 (halaman Settings > Asset Master termuat) mendahului asersi tab `Labels` tidak tampil di langkah 16. Karena `Labels` Hidden, elemen lain matriks (Create, Edit, Delete, Download, View Tagged Assets) tidak terjangkau untuk `DU-64`; sel itu tidak diasersi terpisah.
- Pembagian dalam spec: klausa "selain itu ❌ (Hidden)" baris Group Manager (tab `Labels` Hidden tanpa capability "Manage Asset Master Data") diasersi pada blok `DU-64` (langkah 14 sampai 16) di bawah subjudul `FALB:component-states/disabled-vs-hidden`, supaya ganti akun tidak dibolak-balik; blok `DU-65` (langkah 17 sampai 23) mengasersi sisi capability dengan Permission Create, Update, dan Delete.
- Pembagian klausa lintas spec: `FALB:component-states/disabled-vs-hidden` dikutip spec 037, 058, dan 059; spec ini mengasersi bagian Hidden pada tab `Labels` (role tanpa capability), spec 059 mengasersi `[+ Label]`, `Edit`, dan `Delete` Hidden bagi Read Only, dan spec 037 mengasersi bagian Submit Disabled pada form.
- Temuan PRD: PRD tidak menyatakan elemen yang pasti tampil di Settings > Asset Master bagi role tanpa capability (tab `Asset Name` juga dinaungi "Manage Asset Master Data"), sehingga langkah 15 hanya memakai halaman yang termuat sebagai anchor.
- Temuan PRD: matriks §2.1 baris Group Manager menyebut "tier per user×group" tanpa menyatakan tier yang dimiliki akun `DU-64`; PRD hanya menyatakan bahwa tier Group Manager saja tidak memberi akses. Asersi mengikuti kepemilikan capability "Manage Asset Master Data".
- Temuan PRD: Permission Create, Update, dan Delete pada capability bersifat independen (§2.1); kombinasi sebagian dari Group Manager tidak diasersi karena PRD tidak menyatakan akun sebagian untuk baris ini (kombinasi sebagian diasersi di spec 059 untuk role "Manage Asset Master Data").
