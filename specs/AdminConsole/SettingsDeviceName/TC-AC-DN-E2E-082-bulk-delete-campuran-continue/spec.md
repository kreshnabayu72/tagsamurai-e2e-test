---
id: TC-AC-DN-E2E-082-bulk-delete-campuran-continue
title: "Bulk Delete Campuran: Continue Menghapus Item Bersih dan Kelompok Skip Unit BYO Saja"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-613
  - TC-AC-DN-226
coverage:
  web: automated
---

# Bulk Delete Campuran: Continue Menghapus Item Bersih dan Kelompok Skip Unit BYO Saja

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `RFID Reader` (tiga SKU) dan `Field Radio` (unit BYO Hardware di Company E); #22 relasi SKU dan unit BYO. Keduanya dilewati server saat `[Continue]` sehingga tidak diubah (S-06).
- Data Dinamis milik spec (di-seed di hook `before` lewat Fixture BE; Category `Accessory`, Measurement `Unit`; sisa dihapus di hook `after`): `Bulk Lanjut A {runId}-082` (TC-AC-DN-613), `Bulk Lanjut C {runId}-082` dan `Bulk Lanjut D {runId}-082` (TC-AC-DN-226).
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE) untuk men-seed Device Name milik spec (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO; master Pre-setup #13 dan #14) dan menghapus sisanya di hook `after` bila spec berhenti di tengah.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-613: Dialog dua kelompok Bulk Delete dengan item diblok unit BYO saja menampilkan satu kelompok skip

1. Ketik Search `{runId}-082`, tekan Enter
2. Centang checkbox baris `Bulk Lanjut A {runId}-082`
3. Klik `(←)` pada kotak Search
4. Centang checkbox baris `Field Radio`
5. Klik `Bulk Action` lalu `Delete`
6. Verifikasi judul dialog "Delete Device Names"
7. Verifikasi kelompok akan dihapus berlabel `The following will be deleted:` berisi satu bullet `Bulk Lanjut A {runId}-082`
8. Verifikasi kelompok di-skip berlabel `Skipped: has BYO units` berisi satu bullet `Field Radio`
9. Verifikasi tidak ada kelompok berlabel `Skipped: has SKUs`
10. Verifikasi kalimat penutup `Are you sure you want to continue?`
11. Verifikasi footer: tombol `[Cancel]` dan `[Continue]`
12. Klik `[Continue]`
13. Verifikasi muncul toast sukses: "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
14. Verifikasi baris `Bulk Lanjut A {runId}-082` tidak lagi ada pada List
15. Verifikasi baris `Field Radio` tetap ada pada List
16. Tunggu toast lama hilang otomatis

### TC-AC-DN-226: Konfirmasi Continue pada Bulk Delete campuran menghapus item bersih dan melewati item diblok

17. Ketik Search `{runId}-082`, tekan Enter
18. Centang checkbox baris `Bulk Lanjut C {runId}-082` dan `Bulk Lanjut D {runId}-082`
19. Klik `(←)` pada kotak Search
20. Centang checkbox baris `RFID Reader` dan `Field Radio`
21. Klik `Bulk Action` lalu `Delete`
22. Klik `[Continue]`
23. Verifikasi muncul toast sukses: "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
24. Verifikasi dialog tertutup
25. Verifikasi List di-refresh
26. Verifikasi baris `Bulk Lanjut C {runId}-082` dan `Bulk Lanjut D {runId}-082` tidak lagi ada pada List
27. Verifikasi baris `RFID Reader` dan `Field Radio` tetap ada pada List
28. Verifikasi Bulk Action Bar hilang
29. Verifikasi seleksi kembali ke 0

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-AC-DN-613 sebelum TC-AC-DN-226.
- Langkah penghubung (S-03): langkah 1 dan 17 (Search `{runId}-082` menampilkan record milik spec, R-16); langkah 3 dan 19 (mengosongkan Search agar baris Pre-setup `RFID Reader` dan `Field Radio` pada halaman 1 dapat dicentang; seleksi dipertahankan saat Search berubah); langkah 16 (menunggu toast lama hilang, R-12).
- Record milik spec dipakai sebagai item bersih (S-06) menggantikan `Cable Tester` dan `Door Antenna` pada TC; item diblok tetap baris Pre-setup karena server melewatinya.
- Temuan untuk QA: Post Condition TC-AC-DN-613 dan 226 (entri Delete di Changelog untuk item bersih dan tidak ada untuk item diblok) tidak punya langkah observasi di TC dan tidak diasersi.
