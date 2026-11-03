---
id: TC-AC-DN-E2E-081-bulk-delete-campuran-dialog-dua-kelompok
title: "Bulk Delete Campuran: Dialog Dua Kelompok, Satu Item Bersih, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-225
  - TC-AC-DN-612
  - TC-AC-DN-227
coverage:
  web: automated
---

# Bulk Delete Campuran: Dialog Dua Kelompok, Satu Item Bersih, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester` dan `Door Antenna` (bersih), `RFID Reader` (tiga SKU), `Field Radio` (unit BYO Hardware di Company E); #22 relasi SKU dan unit BYO (disediakan tim FE/BE lewat seed). Dialog tidak pernah dikonfirmasi, sehingga baris Pre-setup tidak diubah (S-06).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-225: Dialog dua kelompok saat Bulk Delete campuran item bersih dan item diblok

1. Centang checkbox baris `Cable Tester`, `Door Antenna`, `RFID Reader`, dan `Field Radio`
2. Klik `Bulk Action` lalu `Delete`
3. Verifikasi judul dialog "Delete Device Names"
4. Verifikasi kelompok akan dihapus berlabel `The following will be deleted:` berisi bullet `Cable Tester` dan `Door Antenna`
5. Verifikasi kelompok di-skip kondisi SKU berlabel `Skipped: has SKUs` berisi bullet `RFID Reader`
6. Verifikasi kelompok di-skip kondisi unit BYO berlabel `Skipped: has BYO units` berisi bullet `Field Radio`
7. Verifikasi alasan SKU dan alasan unit BYO tampil sebagai dua kelompok terpisah, tidak digabung dalam satu label
8. Verifikasi kalimat penutup `Are you sure you want to continue?`
9. Verifikasi footer: tombol `[Cancel]` dan `[Continue]`

### TC-AC-DN-612: Cancel pada dialog dua kelompok Bulk Delete campuran mempertahankan seleksi dan tidak menghapus apa pun

10. Klik `[Cancel]`
11. Verifikasi dialog tertutup
12. Verifikasi tidak ada toast
13. Verifikasi Bulk Action Bar tetap tampil dengan `4 Device Names selected`
14. Verifikasi keempat baris tetap tercentang dan tetap ada pada List
15. Verifikasi tidak ada Device Name yang terhapus

### TC-AC-DN-227: Bulk Delete campuran dengan satu item bersih tetap memakai dialog dua kelompok

16. Hilangkan centang baris `Door Antenna` dan `Field Radio`
17. Klik `Bulk Action` lalu `Delete`
18. Verifikasi kelompok akan dihapus berlabel `The following will be deleted:` berisi satu bullet `Cable Tester`
19. Verifikasi kelompok di-skip berlabel `Skipped: has SKUs` berisi satu bullet `RFID Reader`
20. Verifikasi tidak ada kelompok berlabel `Skipped: has BYO units`
21. Verifikasi footer: tombol `[Cancel]` dan `[Continue]`
22. Klik `[Cancel]`
23. Klik ikon `(X)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC berbeda dari urutan nomor TC; spec ini menjalankan TC-AC-DN-225, 612, 227: TC-AC-DN-612 melanjutkan dialog dua kelompok yang terbuka pada TC-AC-DN-225 (halaman yang sama dipakai berulang tanpa submit).
- Langkah penghubung (S-03, S-09): langkah 16 (mengurangi seleksi menjadi `Cable Tester` dan `RFID Reader` sesuai TC-AC-DN-227); langkah 22 dan 23 (menutup dialog dan membersihkan seleksi).
- Temuan untuk QA: Post Condition TC-AC-DN-612 ("tidak ada record terhapus", "tidak ada entri log baru") tidak punya langkah observasi di TC selain Expected tentang baris; entri log tidak diasersi.
