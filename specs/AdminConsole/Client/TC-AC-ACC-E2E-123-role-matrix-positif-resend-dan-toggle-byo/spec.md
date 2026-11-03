---
id: TC-AC-ACC-E2E-123-role-matrix-positif-resend-dan-toggle-byo
title: "Role Matrix Positif: Resend Activation Email dan Toggle BYO oleh Pemegang Update, Distributor, dan Partner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-617
  - TC-AC-ACC-607
  - TC-AC-ACC-608
  - TC-AC-ACC-609
coverage:
  web: automated
---

# Role Matrix Positif: Resend Activation Email dan Toggle BYO oleh Pemegang Update, Distributor, dan Partner

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (langkah tiap role berbeda target dan aksi, sehingga spec ditulis per blok role dengan Step ganti akun eksplisit; akun pertama login di hook `before`):

| Blok | Role | Akun | Env password | Client target | Aksi |
|---|---|---|---|---|---|
| 1 | Active-Update-Only A-06 (Manage active client: Update + Read, exact-match Area Jakarta) | `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_UPDATE_PASSWORD` | `PT Teknologi Maju {runId}-123` (replika setara C-02) dan `PT Ubah Mitra 17 {runId}-123` (replika setara C-ROL-8) | Resend Activation Email; toggle BYO |
| 2 | Distributor Total Control A-13 (PT Distribusi Nusantara) | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `AC_CLIENT_DIST_TC_PASSWORD` | `PT Teknologi Maju {runId}-123` | Toggle BYO |
| 3 | Partner Total Control A-14 (CV Mitra Sejati) | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `AC_CLIENT_PARTNER_TC_PASSWORD` | `PT Cahaya Baru {runId}-123` (replika setara C-07) | Toggle BYO |

- Login akun blok 1 di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): `PT Teknologi Maju {runId}-123` (setara C-02: Active, FAMS Grace, SAMS dan SIEM No Subscription, Default User Not Yet Activated, Partner CV Mitra Sejati Anchor + CV Mitra Lestari, Group Area Jakarta, toggle BYO awal Disabled), `PT Ubah Mitra 17 {runId}-123` (setara C-ROL-8: Active, satu-satunya Partner CV Mitra Sejati, Group Area Jakarta, tanpa subscription, toggle BYO awal Disabled), dan `PT Cahaya Baru {runId}-123` (setara C-07: Active, Partner CV Mitra Sejati, Group Area Jakarta, FAMS Waiting for Approval, toggle BYO awal Disabled). Efek: toggle BYO digeser ke Enabled, baris Changelog `Edit` Field `Allow Self-Purchased Device Activation` dan Last Updated bertambah; Resend menambah baris Changelog `Resend Activation Email` dan mengirim email; semuanya hanya pada replika milik spec. Client C-02, C-ROL-8 `PT Ubah Mitra 17`, dan C-07 literal tidak disentuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Active-Update-Only

#### TC-AC-ACC-617: Resend Activation Email oleh pemegang Update pada Manage active client sampai sukses

1. Ketik Search `PT Teknologi Maju {runId}-123`, tekan Enter
2. Klik Company Name `PT Teknologi Maju {runId}-123`
3. Klik `[Resend Activation Email]`
4. Verifikasi toast sukses "Success, activation email has been sent."
5. Tunggu aksi selesai (tombol `[Resend Activation Email]` aktif kembali)

#### TC-AC-ACC-607: Toggle BYO Activation Setting oleh pemegang Update sampai sukses

6. Klik breadcrumb "Client", ketik Search `PT Ubah Mitra 17 {runId}-123`, tekan Enter, klik Company Name `PT Ubah Mitra 17 {runId}-123`
7. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled
8. Verifikasi dialog Title "Allow Self-Purchased Device Activation" dengan bullet `• PT Ubah Mitra 17 {runId}-123`
9. Verifikasi dialog memuat "This client will be able to activate devices that were not shipped through the distribution chain. These devices are not pre-verified. Are you sure you want to enable it?"
10. Verifikasi dialog memuat tombol `[Cancel]` dan `[Enable]`
11. Klik `[Enable]`
12. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
13. Verifikasi toggle berstatus Enabled

### Blok 2: Distributor

14. Ganti akun: logout lalu login sebagai Distributor Total Control A-13

#### TC-AC-ACC-608: Toggle BYO Activation Setting oleh Distributor sampai sukses

15. Ketik Search `PT Teknologi Maju {runId}-123`, tekan Enter, klik Company Name `PT Teknologi Maju {runId}-123`
16. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled
17. Verifikasi dialog Title "Allow Self-Purchased Device Activation" dengan bullet `• PT Teknologi Maju {runId}-123`
18. Verifikasi dialog memuat "This client will be able to activate devices that were not shipped through the distribution chain. These devices are not pre-verified. Are you sure you want to enable it?"
19. Verifikasi dialog memuat tombol `[Cancel]` dan `[Enable]`
20. Klik `[Enable]`
21. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
22. Verifikasi toggle berstatus Enabled

### Blok 3: Partner

23. Ganti akun: logout lalu login sebagai Partner Total Control A-14

#### TC-AC-ACC-609: Toggle BYO Activation Setting oleh Partner sampai sukses

24. Ketik Search `PT Cahaya Baru {runId}-123`, tekan Enter, klik Company Name `PT Cahaya Baru {runId}-123`
25. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled
26. Verifikasi dialog Title "Allow Self-Purchased Device Activation" dengan bullet `• PT Cahaya Baru {runId}-123`
27. Verifikasi dialog memuat "This client will be able to activate devices that were not shipped through the distribution chain. These devices are not pre-verified. Are you sure you want to enable it?"
28. Verifikasi dialog memuat tombol `[Cancel]` dan `[Enable]`
29. Klik `[Enable]`
30. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
31. Verifikasi toggle berstatus Enabled

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif ditulis per blok role (bagian 3a): langkah berbeda per role (target dan aksi) dan ganti akun memakai Step eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Kombinasi role × aksi hanya yang punya TC sumber.
- Spec ini memuat 31 langkah: satu `Verifikasi` per klausa Expected (S-01) atas empat TC satu topik (Role Matrix positif Resend dan Toggle BYO); ganti akun lewat Step eksplisit sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras; tiap blok memakai replika sendiri sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): "Tunggu aksi selesai" sesudah Resend (langkah 5, karena langkah berikutnya berpindah surface) dan ganti akun (langkah 14 dan 23). Pemulihan toggle ke Disabled (Post Condition TC-AC-ACC-607 sampai 609) tidak dijalankan karena target adalah replika milik spec yang dibersihkan hook `after`.
- Post Condition TC-AC-ACC-617 (log `Resend Activation Email` Field `Email`) serta TC-AC-ACC-607 sampai 609 butir a (log `Edit` Old `Disabled`, New `Enabled`) tanpa langkah observasi di TC tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACC-617 Precondition b menyebut pengguna berada di Detail "PT Teknologi Maju" sedangkan Langkah hanya "Klik [Resend Activation Email]"; spec membuka Detail lewat Search dan klik Company Name.
  - TC-AC-ACC-608 dan 609 tidak menyebut Post Condition pemulihan selain pada kolom Post Condition; spec memulihkan toggle sesuai kolom itu.
