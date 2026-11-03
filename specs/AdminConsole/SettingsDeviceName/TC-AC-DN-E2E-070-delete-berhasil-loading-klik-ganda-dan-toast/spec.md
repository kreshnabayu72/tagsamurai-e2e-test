---
id: TC-AC-DN-E2E-070-delete-berhasil-loading-klik-ganda-dan-toast
title: "Delete Device Name: Loading, Klik Ganda, dan Toast 4 Detik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-199
  - TC-AC-DN-200
  - TC-AC-DN-187
coverage:
  web: automated
---

# Delete Device Name: Loading, Klik Ganda, dan Toast 4 Detik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Dinamis milik spec (di-seed di hook `before` lewat Fixture BE; Category `Accessory`, Measurement `Unit`): `Delete Loading {runId}-070` (TC-AC-DN-199), `Delete Klik Ganda {runId}-070` (TC-AC-DN-200), `Delete Toast {runId}-070` (TC-AC-DN-187). Ketiganya dihapus oleh langkah spec.
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE) untuk men-seed Device Name milik spec (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO; master Pre-setup #13 dan #14) dan menghapus sisanya di hook `after` bila spec berhenti di tengah.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons request hapus 3 detik di atas backend nyata; intercept dilepas segera setelah respons diterima.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-199: Tombol Delete masuk loading selama request hapus berlangsung

1. Ketik Search `Delete Loading {runId}-070`, tekan Enter
2. Klik ikon aksi pada kolom Actions baris `Delete Loading {runId}-070` lalu klik `Delete`
3. Tunda respons request hapus 3 detik dengan `Spectra.intercept()`
4. Klik `[Delete]`
5. Verifikasi tombol `[Delete]` menampilkan indikator loading selama request berlangsung
6. Verifikasi tombol `[Delete]` tidak dapat diklik ulang selama request berlangsung
7. Tunggu respons yang ditunda diterima, lalu lepas intercept
8. Verifikasi dialog tertutup
9. Verifikasi muncul toast sukses: "Success, device name has been deleted."
10. Tunggu toast lama hilang otomatis

### TC-AC-DN-200: Klik ganda pada tombol Delete hanya menghapus satu kali

11. Ganti isi kotak search dengan `Delete Klik Ganda {runId}-070`, tekan Enter
12. Klik ikon aksi pada kolom Actions baris `Delete Klik Ganda {runId}-070` lalu klik `Delete`
13. Klik `[Delete]` dua kali berturut-turut dengan cepat
14. Verifikasi muncul satu toast sukses: "Success, device name has been deleted."
15. Verifikasi tidak ada toast error kedua
16. Verifikasi baris `Delete Klik Ganda {runId}-070` tidak lagi ada pada List
17. Klik ikon Changelog pada Table Tools
18. Ketik Search `Delete Klik Ganda {runId}-070` pada modal Changelog, tekan Enter
19. Verifikasi modal Changelog menampilkan entri Delete untuk `Delete Klik Ganda {runId}-070` tepat satu kali, tanpa entri ganda
20. Tutup modal Changelog lewat `✕`
21. Tunggu toast lama hilang otomatis

### TC-AC-DN-187: Toast sukses Delete muncul di kanan bawah dan hilang otomatis dalam 4 detik

22. Ganti isi kotak search dengan `Delete Toast {runId}-070`, tekan Enter
23. Klik ikon aksi pada kolom Actions baris `Delete Toast {runId}-070` lalu klik `Delete`
24. Klik `[Delete]`
25. Verifikasi toast berada di kanan bawah layar
26. Verifikasi muncul toast sukses: "Success, device name has been deleted."
27. Tunggu 5 detik tanpa interaksi
28. Verifikasi toast sukses tersebut hilang sendiri setelah 4 detik

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 11, 22 (Search untuk menemukan baris target, R-16); langkah 7 (pelepasan intercept); langkah 10 dan 21 (menunggu toast lama hilang agar hitungan toast berikutnya benar, R-12); langkah 17 sampai 20 (membuka modal Changelog, mencari entri, menutupnya) karena Expected TC-AC-DN-200 butir c menuntut pembacaan Changelog yang tidak ada di Langkah Uji TC.
- Intercept pada langkah 3 hanya menahan respons untuk mengamati state loading; bukan kelas b (bagian 3 prinsip 13).
- Record milik spec dipakai sebagai target hapus (S-06); asersi entri Changelog memakai nama bersuffix unik sehingga baseline nol (S-12).
- Pembagian TC lintas spec: TC-AC-DN-186 (Delete berhasil dan pilihan Device SKU) ada di spec 085.
- Temuan untuk QA: TC-AC-DN-200 tidak menyebut cara menemukan entri di modal Changelog; spec memakai Search modal dengan nama record.
