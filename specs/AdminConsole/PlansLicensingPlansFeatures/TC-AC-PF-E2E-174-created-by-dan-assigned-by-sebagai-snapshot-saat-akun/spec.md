---
id: TC-AC-PF-E2E-174-created-by-dan-assigned-by-sebagai-snapshot-saat-akun
title: "Created By dan Assigned By sebagai nilai tersimpan saat akun pembuat atau pemberi tugas dihapus atau dinonaktifkan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-807
  - TC-AC-PF-808
  - TC-AC-PF-809
coverage:
  web: automated
---

# Created By dan Assigned By sebagai nilai tersimpan saat akun pembuat atau pemberi tugas dihapus atau dinonaktifkan

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang membentuk Dataset Plan UD (akun dihapus atau dinonaktifkan setelah membuat custom plan dan menugaskan client) serta memulihkannya secara idempoten; penghapusan preferensi kolom Plans List Custom Active dan Tab Assigned Clients di browser (disediakan tim FE). Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan UD, tersedia lewat fixture BE; tab Custom Active hanya memuat custom plan Dataset Plan UD. Akun `Maya Putri` dihapus dan akun `Eka Pratama` dinonaktifkan setelah membuat custom plan dan menugaskan client. Custom plan: `Paket Pembuat Hapus` (Created By `Maya Putri`), `Paket Pembuat Nonaktif` (Created By `Eka Pratama`), `Paket Pembuat Aktif` (Created By `Andi Wijaya`), dan `Paket Pemberi Tugas` (Created By `Andi Wijaya`) dengan client `PT Tugas Satu` (Assigned By `Maya Putri`), `PT Tugas Dua` (Assigned By `Eka Pratama`), dan `PT Tugas Tiga` (Assigned By `Jane Smith`). Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec menampilkan kolom `Created By` (konfigurasi kolom tersimpan di browser); hook `after` menghapus preferensi kolom. Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Created By pada Plans List (TC-AC-PF-807)

1. Klik tab `Custom`, sub-tab `Active`.
2. Tampilkan kolom `Created By` lewat Overlay Column Visibility.
3. Verifikasi Created By baris `Paket Pembuat Hapus` tampil `Maya P`.
4. Verifikasi Created By baris `Paket Pembuat Nonaktif` tampil `Eka P`.
5. Verifikasi Created By baris `Paket Pembuat Aktif` tampil `Andi W`.
6. Verifikasi sel Created By ketiga baris tidak kosong dan tidak berisi `—`.
7. Hover sel `Maya P`.
8. Verifikasi tooltip `Maya Putri` tampil.
9. Hover sel `Eka P`.
10. Verifikasi tooltip `Eka Pratama` tampil.

### Sort Created By (TC-AC-PF-809, bagian Plans List)

11. Klik header `Created By` satu kali.
12. Verifikasi `Paket Pembuat Aktif` dan `Paket Pemberi Tugas` (keduanya `Andi Wijaya`) berdampingan di posisi pertama (urutan di antara keduanya tidak dinilai).
13. Verifikasi `Paket Pembuat Nonaktif` (`Eka Pratama`) berada di posisi ketiga.
14. Verifikasi `Paket Pembuat Hapus` (`Maya Putri`) berada di posisi keempat.

### Assigned By pada Tab Assigned Clients (TC-AC-PF-808)

15. Klik `Paket Pemberi Tugas`.
16. Klik Tab Assigned Clients.
17. Verifikasi Assigned By baris `PT Tugas Satu` tampil `Maya P`.
18. Verifikasi Assigned By baris `PT Tugas Dua` tampil `Eka P`.
19. Verifikasi Assigned By baris `PT Tugas Tiga` tampil `Jane S`.
20. Verifikasi sel Assigned By ketiga baris tidak kosong dan tidak berisi `—`.
21. Hover sel `Maya P`.
22. Verifikasi tooltip `Maya Putri` tampil.
23. Hover sel `Eka P`.
24. Verifikasi tooltip `Eka Pratama` tampil.

### Sort dan Filter Assigned By (TC-AC-PF-809, bagian Tab Assigned Clients)

25. Klik header `Assigned By` satu kali.
26. Verifikasi urutan ascending Assigned By: `PT Tugas Dua` (`Eka P`), `PT Tugas Tiga` (`Jane S`), lalu `PT Tugas Satu` (`Maya P`).
27. Buka Filter Panel, buka dropdown Assigned By.
28. Verifikasi dropdown Assigned By memuat opsi `Eka Pratama`, `Jane Smith`, dan `Maya Putri`.
29. Pilih Assigned By `Maya Putri`, klik `[Apply]`.
30. Verifikasi tabel menampilkan hanya baris `PT Tugas Satu`.
31. Hover sel `Maya P` pada baris hasil.
32. Verifikasi tooltip `Maya Putri` tampil.
33. Buka Filter Panel, kosongkan seluruh filter, klik `[Apply]`.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 2 (menampilkan kolom `Created By`, bagian dari TC-AC-PF-807 dan TC-AC-PF-809) dan langkah 33 (mengosongkan filter).
- Urutan TC dalam spec: bagian Plans List TC-AC-PF-809 (langkah 11 sampai 14) ditulis sebelum TC-AC-PF-808 karena keduanya berjalan pada daftar Custom Active yang sudah terbuka dengan kolom `Created By` tampil; bagian Tab Assigned Clients TC-AC-PF-809 (langkah 25 sampai 32) ditulis sesudah TC-AC-PF-808 pada Plan Detail `Paket Pemberi Tugas` yang sama. Dengan begitu perpindahan antara daftar dan Plan Detail terjadi sekali.
- Langkah 12 dan 26 memakai nama tampil kolom (`Maya P`, `Eka P`, `Jane S`) selain nama lengkap tersimpan dari Expected TC, karena sel menampilkan format singkat.
- Temuan untuk QA:
  - Expected TC-AC-PF-809 butir a menyebut urutan di antara dua plan `Andi Wijaya` tidak dinilai; spec mengikuti dan hanya mengasersi bahwa keduanya berada di dua posisi pertama.
  - Expected TC-AC-PF-809 butir b, c, dan d memakai nama lengkap tersimpan (`Eka Pratama`, `Maya Putri`) pada urutan dan opsi dropdown, sedangkan sel tabel menampilkan format singkat.
