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
| 1 | Active-Update-Only A-06 (Manage active client: Update + Read, exact-match Area Jakarta) | `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_UPDATE_PASSWORD` | `PT Teknologi Maju` (C-02) dan `PT Ubah Mitra 17` (C-ROL-8) | Resend Activation Email; toggle BYO |
| 2 | Distributor Total Control A-13 (PT Distribusi Nusantara) | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `AC_CLIENT_DIST_TC_PASSWORD` | `PT Teknologi Maju` | Toggle BYO |
| 3 | Partner Total Control A-14 (CV Mitra Sejati) | `totalControlPartner_automated_cvMitraSejati@qwertysystem.net` | `AC_CLIENT_PARTNER_TC_PASSWORD` | `PT Cahaya Baru` (C-07) | Toggle BYO |

- Login akun blok 1 di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup yang diubah lalu dipulihkan (S-06): toggle BYO `PT Ubah Mitra 17` (C-ROL-8, awal Disabled), `PT Teknologi Maju`, dan `PT Cahaya Baru` (toggle awal Disabled) digeser ke Enabled lalu kembali ke Disabled tanpa dialog. Efek: baris Changelog `Edit` Field `Allow Self-Purchased Device Activation` dan Last Updated bertambah; Resend menambah baris Changelog `Resend Activation Email` dan mengirim email. `PT Teknologi Maju` berstatus Active, Default User Not Yet Activated, FAMS Grace.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Active-Update-Only

#### TC-AC-ACC-617: Resend Activation Email oleh pemegang Update pada Manage active client sampai sukses

1. Ketik Search `PT Teknologi Maju`, tekan Enter
2. Klik Company Name `PT Teknologi Maju`
3. Klik `[Resend Activation Email]`
4. Verifikasi toast sukses "Success, activation email has been sent."
5. Tunggu aksi selesai (tombol `[Resend Activation Email]` aktif kembali)

#### TC-AC-ACC-607: Toggle BYO Activation Setting oleh pemegang Update sampai sukses

6. Klik breadcrumb "Client", ketik Search `PT Ubah Mitra 17`, tekan Enter, klik Company Name `PT Ubah Mitra 17`
7. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled
8. Verifikasi dialog Title "Allow Self-Purchased Device Activation" dengan bullet `• PT Ubah Mitra 17`
9. Verifikasi dialog memuat "This client will be able to activate devices that were not shipped through the distribution chain. These devices are not pre-verified. Are you sure you want to enable it?"
10. Verifikasi dialog memuat tombol `[Cancel]` dan `[Enable]`
11. Klik `[Enable]`
12. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
13. Verifikasi toggle berstatus Enabled
14. Geser toggle ke Disabled
15. Tunggu aksi selesai (toggle berstatus Disabled)

### Blok 2: Distributor

16. Ganti akun: logout lalu login sebagai Distributor Total Control A-13

#### TC-AC-ACC-608: Toggle BYO Activation Setting oleh Distributor sampai sukses

17. Ketik Search `PT Teknologi Maju`, tekan Enter, klik Company Name `PT Teknologi Maju`
18. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled
19. Verifikasi dialog Title "Allow Self-Purchased Device Activation" dengan bullet `• PT Teknologi Maju`
20. Verifikasi dialog memuat "This client will be able to activate devices that were not shipped through the distribution chain. These devices are not pre-verified. Are you sure you want to enable it?"
21. Verifikasi dialog memuat tombol `[Cancel]` dan `[Enable]`
22. Klik `[Enable]`
23. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
24. Verifikasi toggle berstatus Enabled
25. Geser toggle ke Disabled
26. Tunggu aksi selesai (toggle berstatus Disabled)

### Blok 3: Partner

27. Ganti akun: logout lalu login sebagai Partner Total Control A-14

#### TC-AC-ACC-609: Toggle BYO Activation Setting oleh Partner sampai sukses

28. Ketik Search `PT Cahaya Baru`, tekan Enter, klik Company Name `PT Cahaya Baru`
29. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled
30. Verifikasi dialog Title "Allow Self-Purchased Device Activation" dengan bullet `• PT Cahaya Baru`
31. Verifikasi dialog memuat "This client will be able to activate devices that were not shipped through the distribution chain. These devices are not pre-verified. Are you sure you want to enable it?"
32. Verifikasi dialog memuat tombol `[Cancel]` dan `[Enable]`
33. Klik `[Enable]`
34. Verifikasi toast sukses "Success, self-purchased device activation setting has been updated."
35. Verifikasi toggle berstatus Enabled
36. Geser toggle ke Disabled

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif ditulis per blok role (bagian 3a): langkah berbeda per role (target dan aksi) dan ganti akun memakai Step eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Kombinasi role × aksi hanya yang punya TC sumber.
- Spec ini melewati 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas empat TC satu topik (Role Matrix positif Resend dan Toggle BYO); ganti akun lewat Step eksplisit sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras; tiap blok memulihkan toggle ke Disabled sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): "Tunggu aksi selesai" sesudah Resend (langkah 5, karena langkah berikutnya berpindah surface), pemulihan toggle ke Disabled tanpa dialog (langkah 14, 25, 36; Post Condition TC-AC-ACC-607 sampai 609), "Tunggu aksi selesai" sesudah pemulihan toggle sebelum ganti akun (langkah 15 dan 26; butir 8 bagian 8b), dan ganti akun (langkah 16 dan 27).
- Post Condition TC-AC-ACC-617 (log `Resend Activation Email` Field `Email`) serta TC-AC-ACC-607 sampai 609 butir a (log `Edit` Old `Disabled`, New `Enabled`) tanpa langkah observasi di TC tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACC-617 Precondition b menyebut pengguna berada di Detail "PT Teknologi Maju" sedangkan Langkah hanya "Klik [Resend Activation Email]"; spec membuka Detail lewat Search dan klik Company Name.
  - TC-AC-ACC-608 dan 609 tidak menyebut Post Condition pemulihan selain pada kolom Post Condition; spec memulihkan toggle sesuai kolom itu.
