---
id: TC-AC-DN-E2E-080-bulk-delete-bersih-berhasil
title: "Bulk Delete Item Bersih: Satu Baris, Klik Ganda, Seleksi di Luar Search, dan Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-224
  - TC-AC-DN-237
  - TC-AC-DN-239
  - TC-AC-DN-223
coverage:
  web: automated
---

# Bulk Delete Item Bersih: Satu Baris, Klik Ganda, Seleksi di Luar Search, dan Berhasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Dinamis milik spec (di-seed di hook `before` lewat Fixture BE; Category `Accessory`, Measurement `Unit`; sisa dihapus di hook `after`): `Bulk Dua A {runId}-080` dan `Bulk Dua B {runId}-080` (TC-AC-DN-224 dan 237), `Bulk Search A {runId}-080` dan `Bulk Search B {runId}-080` (TC-AC-DN-239), `Bulk Berhasil A {runId}-080` dan `Bulk Berhasil B {runId}-080` (TC-AC-DN-223).
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE) untuk men-seed Device Name milik spec (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO; master Pre-setup #13 dan #14) dan menghapus sisanya di hook `after` bila spec berhenti di tengah.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-224: Bulk Action Bar dengan satu baris memakai dialog konfirmasi single

1. Ketik Search `{runId}-080`, tekan Enter
2. Centang checkbox baris `Bulk Dua A {runId}-080`
3. Klik `Bulk Action` lalu `Delete`
4. Verifikasi judul dialog "Delete Device Name" dalam bentuk singular
5. Verifikasi body: satu bullet `Bulk Dua A {runId}-080`
6. Verifikasi body: kalimat penutup `Are you sure you want to delete it? This action cannot be undone.`
7. Verifikasi footer: tombol `[Cancel]` dan `[Delete]`
8. Klik `[Cancel]`

### TC-AC-DN-237: Klik ganda pada tombol Delete dialog Bulk Delete hanya memproses satu kali

9. Centang checkbox baris `Bulk Dua B {runId}-080`
10. Klik `Bulk Action` lalu `Delete`
11. Klik `[Delete]` dua kali berturut-turut dengan cepat
12. Verifikasi muncul satu toast sukses: "Success, device name has been deleted."
13. Verifikasi tidak ada toast kedua
14. Klik ikon Changelog pada Table Tools
15. Ketik Search `Bulk Dua` pada modal Changelog, tekan Enter
16. Verifikasi modal Changelog memuat entri Delete untuk `Bulk Dua A {runId}-080` tepat satu kali
17. Verifikasi modal Changelog memuat entri Delete untuk `Bulk Dua B {runId}-080` tepat satu kali
18. Tutup modal Changelog lewat `✕`
19. Tunggu toast lama hilang otomatis

### TC-AC-DN-239: Bulk Delete memproses seluruh seleksi termasuk baris yang tidak tampil karena Search

20. Ganti isi kotak search dengan `Bulk Search A {runId}-080`, tekan Enter
21. Centang baris `Bulk Search A {runId}-080`
22. Ganti isi kotak search dengan `Bulk Search B {runId}-080`, tekan Enter
23. Centang baris `Bulk Search B {runId}-080`
24. Verifikasi counter sebelum dialog `2 Device Names selected` walau hanya satu baris tampil
25. Klik `Bulk Action` lalu `Delete`
26. Verifikasi dialog `Delete Device Names` memuat bullet `Bulk Search A {runId}-080` dan `Bulk Search B {runId}-080`
27. Klik `[Delete]`
28. Verifikasi muncul toast sukses: "Success, device name has been deleted."
29. Klik `(←)` pada kotak Search
30. Verifikasi `Bulk Search A {runId}-080` dan `Bulk Search B {runId}-080` tidak ada pada List

### TC-AC-DN-223: Bulk Delete seluruh item bersih berhasil

31. Ketik Search `Bulk Berhasil`, tekan Enter
32. Centang checkbox baris `Bulk Berhasil A {runId}-080` dan `Bulk Berhasil B {runId}-080`
33. Klik `Bulk Action` lalu `Delete`
34. Klik `[Delete]` pada dialog
35. Verifikasi muncul toast sukses: "Success, device name has been deleted."
36. Verifikasi dialog tertutup
37. Verifikasi List di-refresh
38. Verifikasi baris `Bulk Berhasil A {runId}-080` dan `Bulk Berhasil B {runId}-080` tidak lagi ada pada List
39. Verifikasi Bulk Action Bar hilang
40. Verifikasi seleksi kembali ke 0

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Alasan lebih dari sekitar 35 langkah: semua blok satu kelas harness (fungsional) dan satu topik (Bulk Delete item bersih) dengan record milik spec yang terpisah per TC; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna (R3).
- Langkah penghubung (S-03): langkah 1, 20, 22, 31 (Search untuk menemukan baris target, R-16; Search `{runId}-080` pada langkah 1 menampilkan semua record milik spec); langkah 8 (menutup dialog); langkah 14 sampai 18 (membuka modal Changelog, mencari entri, menutupnya, karena Expected TC-AC-DN-237 butir b menuntut pembacaan Changelog); langkah 19 (menunggu toast lama hilang, R-12); langkah 29 (mengosongkan Search, sesuai Expected TC-AC-DN-239 butir d).
- TC-AC-DN-224 dan TC-AC-DN-237 memakai seleksi bersama: `Bulk Dua A` tetap tercentang setelah `[Cancel]` pada langkah 8 dan ikut dihapus pada TC-AC-DN-237 (langkah awal TC itu identik).
- Record milik spec dipakai sebagai target hapus (S-06) menggantikan `Cable Tester` dan `Door Antenna` pada TC; asersi entri Changelog memakai nama bersuffix unik sehingga baseline nol (S-12).
- Temuan untuk QA:
  - TC-AC-DN-223 Post Condition b (penghapusan tercatat pada Changelog, Activity Log, dan System Log aktor) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-AC-DN-237 tidak menyebut cara menemukan entri di modal Changelog; spec memakai Search modal dengan nama record.
