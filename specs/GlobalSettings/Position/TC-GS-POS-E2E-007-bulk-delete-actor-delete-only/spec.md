---
id: TC-GS-POS-E2E-007-bulk-delete-actor-delete-only
title: Bulk Delete Position oleh actor Delete-Only
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-124
  - TC-GS-POS-125
coverage:
  web: automated
---

# Bulk Delete Position oleh actor Delete-Only

## Prerequisites

- Spec ini pasangan dari spec 005 dan spec 006. Spec 005 membuktikan checkbox dan Bulk Action Bar
  terlihat bagi role ini, spec 006 membuktikan Delete single berhasil. Spec ini menutup jalur
 ketiga, yaitu Bulk Delete, yang punya popup konfirmasi dengan bentuk berbeda.
- Login dilakukan sebagai Role Delete-Only, bukan akun Total Control. Akun bercapability khusus ini
  adalah syarat jalannya spec.
- `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD` hanya dipakai menyiapkan data awal
  lewat Total Control. Penghapusan yang diuji dilakukan oleh akun Delete-Only.
- Kedua Position target dibuat lebih dulu lewat akun Total Control dan dipastikan tidak
  direferensikan user mana pun. Kalau ternyata direferensikan, server menolak penghapusan dan toast
  sukses tidak akan pernah muncul, sehingga kegagalan test tidak bisa dibedakan antara bug permission
  dan referensi data.
- Satu Position pengontrol, yaitu
  `Fixture.globalSettingsPosition.bulkDelete.controlName`, sengaja ikut disiapkan dan tidak ikut
  dicentang, supaya terbukti bahwa Bulk Delete hanya menyentuh yang dicentang.
- `Fixture.globalSettingsPosition.captions.toast` adalah pemformatan toast sukses modul, yaitu
  `Success, position has been deleted.`
- `Fixture.globalSettingsPosition.captions.bulkActionBar` adalah area tombol aksi di bawah tabel
  yang muncul hanya ketika ada baris yang dicentang.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteConfirm` adalah judul popup konfirmasi
  Bulk Delete.
- `Fixture.globalSettingsPosition.bulkDelete.targets` adalah dua Position yang dicentang, yaitu
  `Night Auditor` dan `Weekend Cashier`.

## Test Steps

### Bulk Delete dua Position sekaligus

1. Login sebagai Total Control
2. Buat kedua Position di
   `Fixture.globalSettingsPosition.bulkDelete.targets`, yaitu `Night Auditor` dan `Weekend Cashier`
3. Buat Position pengontrol
   `Fixture.globalSettingsPosition.bulkDelete.controlName`
4. Verifikasi ketiga Position tampil di tabel
5. Keluar dari akun Total Control
6. Login sebagai Role Delete-Only
7. Verifikasi tab `Position` terbuka dan ketiga Position dapat dibaca
8. Verifikasi tombol `[+ Position]` tidak tampil, sesuai capability yang dimiliki
9. Verifikasi kolom Checkbox seleksi tampil di header tabel
10. Verifikasi kolom Checkbox seleksi tampil di setiap baris body tabel
11. Verifikasi Bulk Action Bar tidak tampil pada kondisi awal, sebelum ada baris dicentang
12. Centang baris `Night Auditor`
13. Verifikasi Bulk Action Bar muncul
14. Verifikasi hanya satu baris yang tercatat terpilih
15. Centang baris `Weekend Cashier`
16. Verifikasi Bulk Action Bar tetap tampil
17. Verifikasi jumlah baris terpilih menjadi dua
18. Verifikasi Position pengontrol `Fixture.globalSettingsPosition.bulkDelete.controlName` tidak
    ikut terpilih karena tidak dicentang
19. Klik tombol `[Delete]` pada Bulk Action Bar
20. Verifikasi popup konfirmasi Bulk Delete muncul
21. Verifikasi popup konfirmasi menyebut jumlah dua record yang akan dihapus
22. Verifikasi popup konfirmasi memuat nama kedua Position, sehingga tidak ambigu apa yang akan dihapus
23. Verifikasi popup konfirmasi memuat peringatan bahwa aksi ini tidak dapat dibatalkan
24. Verifikasi tabel belum berubah pada saat popup masih terbuka, sehingga pembatalan masih mungkin
25. Klik tombol `[Delete]` pada popup konfirmasi
26. Verifikasi toast sukses `Success, position has been deleted.` muncul
27. Verifikasi popup konfirmasi tertutup
28. Verifikasi baris `Night Auditor` tidak lagi ada di tabel
29. Verifikasi baris `Weekend Cashier` tidak lagi ada di tabel
30. Verifikasi baris `Fixture.globalSettingsPosition.bulkDelete.controlName` masih ada di tabel
31. Verifikasi jumlah baris berkurang tepat dua, tidak ada baris lain yang ikut hilang
32. Verifikasi jumlah total data pada server berkurang tepat dua setelah memuat ulang halaman
33. Verifikasi Bulk Action Bar hilang setelah tidak ada lagi baris terpilih
34. Verifikasi checkbox header tercentang penuh, sehingga baru bisa dipakai untuk seleksi ulang baris
    yang tersisa

### Pembatalan popup konfirmasi tidak menghapus apa pun

35. Siapkan ulang kedua Position target di
    `Fixture.globalSettingsPosition.bulkDelete.targets`
36. Verifikasi keduanya tampil di tabel
37. Centang kedua baris tersebut
38. Verifikasi Bulk Action Bar muncul dan jumlah terpilih adalah dua
39. Klik tombol `[Delete]` pada Bulk Action Bar
40. Verifikasi popup konfirmasi Bulk Delete muncul
41. Klik tombol pembatalan pada popup konfirmasi
42. Verifikasi popup tertutup
43. Verifikasi tidak ada toast sukses yang muncul
44. Verifikasi kedua Position target masih ada di tabel
45. Verifikasi jumlah baris tidak berubah

### Penolakan server terhadap Bulk Delete di tengah seleksi

46. Siapkan ulang kedua Position target, lalu centang keduanya sehingga Bulk Action Bar muncul
47. Verifikasi jumlah baris terpilih adalah dua
48. Klik tombol `[Delete]` pada Bulk Action Bar
49. Verifikasi popup konfirmasi Bulk Delete muncul
50. Klik tombol `[Delete]` pada popup konfirmasi
51. Verifikasi server menolak aksi dan toast error muncul
52. Verifikasi tabel tidak menunjukkan hilangnya baris manapun
53. Verifikasi kedua Position target masih ada di tabel setelah memuat ulang halaman
54. Verifikasi jumlah baris terpilih masih tercatat, sehingga pengguna bisa mencoba ulang atau
    membatalkan aksi

## Notes

- Toast sukses yang diharapkan masih `Success, position has been deleted.` untuk kedua record,
  mengikuti TC-GS-POS-125. PRD tidak menetapkan bentuk toast plural, jadi spec ini tidak mengarang
  bentuk lain seperti `2 positions have been deleted.`
- Popup konfirmasi Bulk Delete dipecah detail per field pada langkah 20 sampai 23 karena bentuknya
  berbeda dari popup konfirmasi Delete single di spec 006. Menggabungkannya akan kehilangan
  pembuktian bahwa Bulk Delete punya konfirmasi sendiri, bukan memakai popup yang sama.
- Position pengontrol ditambahkan supaya test tidak hanya membuktikan dua baris hilang, tetapi juga
  bahwa hanya baris yang dicentang yang hilang. Tanpa pengontrol, ada bug yang membuat seluruh
  tabel terkirim dalam bulk request yang akan tetap lulus pada test ini.
- Subbagian pembatalan dan penolakan server sengaja memakai data yang disiap ulang di tiap
  subbagian, bukan mengandalkan sisa subbagian sebelumnya. Spec lain di suite ini memakai pola
  seed per subbagian dengan alasan yang sama.
- Langkah 24 memeriksa tabel belum berubah selagi popup terbuka. Ini yang membuat pembatalan
  pada langkah 41 punya makna; kalau server sudah memproses sebelum konfirmasi, pembatalan hanya
  jadi hiasan.
- Langkah 34 memeriksa checkbox header tercentang penuh setelah penghapusan. Kondisi ini yang
  membuat Bulk Action Bar dan seleksi berikutnya bisa dipakai, jadi bukan sekadar detail tampilan.
