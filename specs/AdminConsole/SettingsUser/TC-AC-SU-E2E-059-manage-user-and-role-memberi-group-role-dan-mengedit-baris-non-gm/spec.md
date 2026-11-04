---
id: TC-AC-SU-E2E-059-manage-user-and-role-memberi-group-role-dan-mengedit-baris-non-gm
title: "Aktor Manage user and role: Memberi Group Role Target Standar dan Mengedit Baris Non-GM"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-213
  - TC-AC-SU-244
coverage:
  web: automated
---

# Aktor Manage user and role: Memberi Group Role Target Standar dan Mengedit Baris Non-GM

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user and role (Update aktif), `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-059` tanpa tingkat akses dan bukan Group Manager dengan `Manage partner` tanpa group assignment; `Dedi Kurnia {runId}-059` (Group Manager di `Region A {runId}-059`) dengan `Manage partner` aktif di `Region A {runId}-059` dan `Region B {runId}-059` (R saja).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-059`): `Region A {runId}-059` > `Branch 1 {runId}-059` > `Floor 1 {runId}-059`; `Region A {runId}-059` > `Branch 3 {runId}-059`; `Region B {runId}-059`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-059@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-059`.
- Env var `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan pemilik repo.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-059` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-213: Aktor Manage user and role memberi Group Role target standar sampai sukses

1. Ketik Search `Budi Santoso {runId}-059`, tekan Enter
2. Klik nama `Budi Santoso {runId}-059` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage partner`
5. Klik `[+ Assign Group]`
6. Centang `Region B {runId}-059` di Popup Select Group, klik `[Select]`
7. Klik `[Save]`
8. Verifikasi kolom Group `Manage partner` menampilkan badge `Region B {runId}-059`, menandai role aktif
9. Verifikasi muncul toast sukses: "Success, group role has been assigned."
10. Klik segmen `User` pada Breadcrumb untuk kembali ke User List

### TC-AC-SU-244: Aktor Manage user and role mengedit baris non-GM pada target Group Manager sampai sukses

11. Tunggu toast lama hilang otomatis
12. Ganti isi kotak Search dengan `Dedi Kurnia {runId}-059`, tekan Enter
13. Klik nama `Dedi Kurnia {runId}-059` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
14. Klik Sub-tab [Group Role]
15. Klik `[Assign Group]` baris `Manage partner`
16. Centang C baris `Region B {runId}-059`
17. Klik `[Save]`
18. Verifikasi muncul toast sukses: "Success, group role has been updated."
19. Verifikasi tidak ada dialog Auto-Revert (group Group Manager tidak berubah)
20. Verifikasi banner tetap `"This user is a Group Manager for: Region A {runId}-059."`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 11, 12 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-209, 242, 243 ada di spec 058.
- Temuan untuk QA:
  - Post Condition TC-213 ("Modified By baris Budi Santoso = aktor Manage user and role") dan TC-244 ("Status Group Manager Region A tetap") tidak punya langkah observasi dan tidak diasersi.
  - Expected TC-213 butir a memuat "role aktif" tanpa elemen UI terpisah; spec memakai badge Group sebagai penanda.
