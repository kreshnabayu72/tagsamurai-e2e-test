---
id: TC-AC-DN-E2E-071-delete-blok-karena-sku
title: "Delete Device Name Diblok karena SKU: Dialog Blok, Tutup, SKU Tunggal, dan Stok Nol"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-188
  - TC-AC-DN-189
  - TC-AC-DN-192
  - TC-AC-DN-591
coverage:
  web: automated
---

# Delete Device Name Diblok karena SKU: Dialog Blok, Tutup, SKU Tunggal, dan Stok Nol

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `RFID Reader` (tiga SKU), `Legacy Scanner` (satu SKU Brand D/Model L1), `NFC Tag` (SKU Brand A/Model N1); #18 `NFC Tag` Company A Total SKU 1, Total Stock 0; #22 relasi SKU (disediakan tim FE/BE lewat seed). Semua aksi ditolak dialog blok sehingga baris Pre-setup tidak diubah (S-06).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-188: Delete Device Name yang masih punya SKU ditolak dengan dialog blok

1. Ketik Search `RFID Reader`, tekan Enter
2. Klik ikon aksi pada kolom Actions baris `RFID Reader` lalu klik `Delete`
3. Verifikasi judul dialog blok "Cannot Delete Device Name"
4. Verifikasi body: daftar nama berisi bullet `RFID Reader`
5. Verifikasi body: pesan alasan blok SKU "This device name still has SKUs."
6. Verifikasi footer: hanya satu tombol `[OK]`
7. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil sebelum dialog blok
8. Verifikasi tidak ada toast
9. Verifikasi baris `RFID Reader` tetap ada pada List dan tidak ada record yang terhapus

### TC-AC-DN-189: Dialog blok Delete hanya ditutup lewat tombol OK atau Esc dan tidak lewat klik backdrop

10. Klik area gelap di luar dialog
11. Verifikasi dialog blok tetap terbuka
12. Verifikasi tidak ada toast
13. Klik `[OK]`
14. Verifikasi dialog tertutup
15. Verifikasi List tampil tanpa perubahan
16. Verifikasi tidak ada toast
17. Verifikasi baris `RFID Reader` tetap ada pada List

### TC-AC-DN-192: Delete Device Name yang hanya memiliki satu SKU tanpa unit BYO ditolak dengan dialog blok

18. Ganti isi kotak search dengan `Legacy Scanner`, tekan Enter
19. Klik ikon aksi pada kolom Actions baris `Legacy Scanner` lalu klik `Delete`
20. Verifikasi judul dialog blok "Cannot Delete Device Name"
21. Verifikasi body: daftar nama berisi bullet `Legacy Scanner`
22. Verifikasi body: pesan alasan blok SKU "This device name still has SKUs."
23. Verifikasi footer: hanya satu tombol `[OK]`
24. Verifikasi dialog konfirmasi `Delete Device Name` tidak tampil sebelum dialog blok
25. Verifikasi tidak ada toast sukses "Success, device name has been deleted." dan tidak ada toast error "Error, failed to delete device name."
26. Verifikasi baris `Legacy Scanner` tetap ada pada List
27. Klik `[OK]`

### TC-AC-DN-591: Delete Device Name yang SKU-nya bersetok nol tetap diblok

28. Ganti isi kotak search dengan `NFC Tag`, tekan Enter
29. Klik menu aksi pada baris `NFC Tag` lalu klik `Delete`
30. Verifikasi dialog blok `D-01` berjudul "Cannot Delete Device Name" dengan bullet `NFC Tag`, teks "This device name still has SKUs.", dan tombol `[OK]`
31. Verifikasi dialog konfirmasi "Delete Device Name" tidak tampil sebelum dialog blok
32. Verifikasi tidak ada toast
33. Klik `[OK]`
34. Verifikasi dialog blok tertutup
35. Verifikasi dialog konfirmasi "Delete Device Name" tidak tampil sesudah dialog blok
36. Verifikasi baris `NFC Tag` tetap ada pada List

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Alasan lebih dari sekitar 35 langkah: semua blok satu kelas harness (fungsional), satu topik (Delete diblok karena SKU) dan satu dataset baca-saja; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna (R3).
- Langkah penghubung (S-03): langkah 1, 18, 28 (Search untuk menemukan baris target, R-16); langkah 27 (menutup dialog blok sebelum TC berikutnya).
- Halaman yang sama dipakai berulang tanpa submit: TC-AC-DN-189 melanjutkan dialog blok yang terbuka pada TC-AC-DN-188 (langkah 10).
- Temuan untuk QA: Post Condition TC-AC-DN-188, 192, dan 591 ("tidak ada entri log baru", "record tetap tersimpan") tidak punya langkah observasi di TC, sehingga tidak diasersi.
