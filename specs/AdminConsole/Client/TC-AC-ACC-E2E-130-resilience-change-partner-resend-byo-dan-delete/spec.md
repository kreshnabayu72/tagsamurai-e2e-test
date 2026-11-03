---
id: TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete
title: "Resilience Change Partner, Resend Activation Email, Toggle BYO, dan Delete: 5xx, Email Service Gagal, Global Settings, dan State Basi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-186
  - TC-AC-ACC-173
  - TC-AC-ACC-171
  - TC-AC-ACC-250
  - TC-AC-ACC-226
  - TC-AC-ACC-227
coverage:
  web: automated
---

# Resilience Change Partner, Resend Activation Email, Toggle BYO, dan Delete: 5xx, Email Service Gagal, Global Settings, dan State Basi

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan kegagalan sisi server; asersi memakai state backend nyata sehingga bukan `Mode: mock`).
- Akun aktor (urutan blok = urutan akun, Step ganti akun eksplisit):
  - Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD` (TC-AC-ACC-186). Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD` (TC-AC-ACC-173, 171, 250).
  - Archived-Delete-Only A-10 `archivedDeleteJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ARCHIVED_DELETE_PASSWORD` (TC-AC-ACC-226, 227).
  - Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca; semua aksi gagal sehingga data tidak berubah): C-13 `PT Ganti Mitra` (hanya CV Mitra Sejati); C-02 `PT Teknologi Maju` (Default User Not Yet Activated, FAMS Grace); C-01 `PT Sejahtera Abadi` (toggle BYO Disabled); C-04 `PT Karya Abadi` (Archived, 2 user ber-App Access). Data milik spec untuk TC-AC-ACC-171 (Dinamis, dibuat lewat API di hook `before`): `PT Resend Basi {runId}-130` (Active, FAMS Active, Default User Not Yet Activated).
- Kemampuan teknis: `Spectra.intercept()` untuk respons 500 pada request [Confirm] Change Partner (TC-AC-ACC-186), 500 pada toggle BYO (TC-AC-ACC-250), dan 500 pada [Delete] (TC-AC-ACC-227), dilepas segera setelah pemicu selesai (S-09); memaksa email service gagal (TC-AC-ACC-173) dan Global Settings tidak terjangkau (TC-AC-ACC-226) sebagai kegagalan sisi server (disediakan tim FE/BE; dipulihkan di hook `after`); aktivasi akun Default User `PT Resend Basi {runId}-130` lewat Fixture BE hingga status Activated tersimpan (TC-AC-ACC-171; pelaku kedua berupa sesi API/fixture, bukan konteks UI kedua).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-186: Change Partner gagal 5xx: toast error T-06, dialog tetap terbuka, dan relasi Partner tidak berubah

1. Ketik Search `PT Ganti Mitra`, tekan Enter
2. Klik `[⋯]` pada baris `PT Ganti Mitra` → klik `Change Partner`
3. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
4. Pasang intercept respons 500 pada request `[Confirm]`
5. Klik `[Confirm]`
6. Verifikasi toast error "Error, failed to update partner."
7. Verifikasi dialog Change Partner tetap terbuka
8. Lepas intercept respons 500
9. Klik `[✕]` pada header dialog
10. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
11. Klik `[Leave]` pada dialog Unsaved Changes
12. Verifikasi Managed By baris `PT Ganti Mitra` adalah "CV Mitra Sejati" tanpa teks `+1 more`

### Blok Active-Full

13. Ganti akun: logout lalu login sebagai Active-Full A-15

#### TC-AC-ACC-173: Email service gagal saat Resend

14. Paksa email service gagal
15. Ketik Search `PT Teknologi Maju`, tekan Enter, klik Company Name `PT Teknologi Maju`
16. Klik `[Resend Activation Email]`
17. Verifikasi toast error "Error, failed to send activation email."
18. Verifikasi badge Default User tetap "Not Yet Activated"
19. Pulihkan email service

#### TC-AC-ACC-171: Server me-re-cek kondisi Resend; state basi ditolak

20. Klik breadcrumb "Client", ketik Search `PT Resend Basi {runId}-130`, tekan Enter, klik Company Name `PT Resend Basi {runId}-130`
21. Verifikasi section Default User menampilkan badge "Not Yet Activated"
22. Aktivasi akun Default User `PT Resend Basi {runId}-130` lewat Fixture BE hingga status Activated tersimpan
23. Klik `[Resend Activation Email]` pada halaman yang belum dimuat ulang
24. Verifikasi toast error "Error, failed to send activation email."

#### TC-AC-ACC-250: Penyimpanan toggle gagal: toggle kembali ke nilai semula

25. Klik breadcrumb "Client", ketik Search `PT Sejahtera Abadi`, tekan Enter, klik Company Name `PT Sejahtera Abadi`
26. Pasang intercept respons 500 pada request toggle BYO
27. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled, lalu klik `[Enable]` pada dialog
28. Verifikasi toast error "Error, failed to update self-purchased device activation setting."
29. Verifikasi toggle kembali ke nilai semula (Disabled)
30. Lepas intercept respons 500

### Blok Archived-Delete-Only

31. Ganti akun: logout lalu login sebagai Archived-Delete-Only A-10

#### TC-AC-ACC-226: Global Settings tidak terjangkau saat Delete

32. Paksa Global Settings tidak terjangkau
33. Klik sub-tab Archived, ketik Search `PT Karya Abadi`, tekan Enter
34. Klik `[⋯]` pada baris `PT Karya Abadi` → klik `Delete`
35. Ketik nama persis `PT Karya Abadi` pada input "Type the client name to confirm", centang "I understand this action cannot be undone", klik `[Delete]`
36. Verifikasi toast error "Error, failed to delete client."
37. Verifikasi dialog "Delete Client" tetap terbuka dengan nama Client yang diketik `PT Karya Abadi`
38. Verifikasi checkbox "I understand this action cannot be undone" tetap terisi
39. Verifikasi tombol `[Delete]` kembali enabled (retry manual)
40. Pulihkan Global Settings terjangkau
41. Klik `[Cancel]` pada dialog "Delete Client"
42. Muat ulang List
43. Klik sub-tab Archived, ketik Search `PT Karya Abadi`, tekan Enter
44. Verifikasi baris `PT Karya Abadi` tetap tampil di sub-tab Archived

#### TC-AC-ACC-227: Delete gagal 5xx: dialog tetap terbuka

45. Klik `[⋯]` pada baris `PT Karya Abadi` → klik `Delete`
46. Ketik nama persis `PT Karya Abadi` pada input "Type the client name to confirm" dan centang "I understand this action cannot be undone"
47. Pasang intercept respons 500 pada request `[Delete]`
48. Klik `[Delete]`
49. Verifikasi toast error "Error, failed to delete client."
50. Verifikasi dialog "Delete Client" tetap terbuka
51. Lepas intercept respons 500
52. Klik `[Cancel]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas enam TC satu kelas harness (fault injection dan state basi pada aksi Detail dan Delete) dengan tiga akun; ganti akun lewat Step eksplisit sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras; tiap blok memakai Client dan pemicu sendiri. Pemicu kegagalan (intercept, GS, email service) adalah objek uji, sehingga tidak memakai `P-2`.
- `P-2` tidak dipakai untuk TC-AC-ACC-171: aktivasi akun oleh pelaku kedua memakai Fixture BE (bukan konteks UI kedua) dan hanya memicu state basi.
- Langkah penghubung (tanpa awalan Verifikasi): memulihkan email service, Global Settings, dan melepas intercept (langkah 8, 19, 30, 40, 51; S-09), `[✕]` dan `[Leave]` penutup dialog dirty (langkah 9 dan 11; Langkah 6 TC-AC-ACC-186), `[Cancel]` penutup dialog (langkah 41 dan 52; pada TC-AC-ACC-226 dialog diasersi tetap terbuka lebih dulu), ganti akun (langkah 13 dan 31), dan muat ulang List.
- Post Condition TC-AC-ACC-186, 173, 171, 250, 227: `-`; TC-AC-ACC-226 ("Client PT Karya Abadi tidak berubah") diwujudkan sebagai langkah 43 dan 44.
- Temuan untuk QA:
  - TC-AC-ACC-173 dan 227 tidak menyebut Client target; spec memakai C-02 dan C-04. TC-AC-ACC-171 tidak menyebut Client; spec memakai Client bersuffix milik spec karena aktivasi Default User tidak dapat dipulihkan (Dikonsumsi).
  - TC-AC-ACC-250 langkah 1 ("geser toggle ke Disabled/Enabled") ambigu; spec memakai geser ke Enabled lalu `[Enable]` karena toggle `PT Sejahtera Abadi` Disabled.
  - TC-AC-ACC-173 dan 171 Expected "tidak ada perubahan state" tidak menyebut state yang diamati; spec mengasersi badge Default User pada TC-AC-ACC-173 dan tidak menambah asersi pada TC-AC-ACC-171.
