---
id: TC-AC-SG-E2E-059-modal-setup-column-tabel-utama-screening-preview-save-dan-tutup-tanpa-save
title: "Modal Setup Column Tabel Utama: Screening, Preview, Save, dan Tutup Tanpa Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-214
  - TC-AC-SG-215
  - TC-AC-SG-216
coverage:
  web: automated
---

# Modal Setup Column Tabel Utama: Screening, Preview, Save, dan Tutup Tanpa Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16), node `All Groups` terpilih, 14 group.
- Kelima kolom data (Group, Total User, Total Member, Modified By, Last Updated) tampil secara default. Spec ini menyimpan konfigurasi kolom lewat `[Save]` (langkah 14): hook `before` dan `after` spec ini menghapus preferensi kolom tabel di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; lihat `suite.md`).
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-214: Screening modal Setup Column tabel utama

1. Klik header kolom Actions `⋯` untuk membuka Overlay Column Visibility
2. Klik `Setup Column...`
3. Verifikasi modal berjudul `Setup Column` dengan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
4. Verifikasi ikon close `[✕]` tampil di modal
5. Verifikasi daftar baris untuk lima kolom data: Group, Total User, Total Member, Modified By, dan Last Updated
6. Verifikasi tiap baris kolom memiliki checkbox
7. Verifikasi tiap baris kolom memiliki handle drag
8. Verifikasi tiap baris kolom memiliki ikon Pin
9. Verifikasi kolom Checkbox dan Actions tidak tercantum di daftar
10. Verifikasi footer `[Reset to Default]` (teks, primary) dan `[Save]` (filled, success)
11. Verifikasi tidak ada tombol `[Cancel]` di footer

### TC-AC-SG-215: Perubahan di modal Setup Column di-preview lalu tersimpan setelah Save

12. Hapus centang Total Member dan Modified By
13. Verifikasi tabel di balik modal langsung menampilkan preview tanpa kolom Total Member dan Modified By
14. Klik `[Save]`
15. Verifikasi modal Setup Column tertutup
16. Verifikasi tabel mempertahankan kolom Total Member dan Modified By disembunyikan
17. Refresh browser (F5)
18. Verifikasi pengaturan tetap tersimpan: kolom Total Member dan Modified By tetap tersembunyi (cache browser)

### TC-AC-SG-216: Menutup modal Setup Column tanpa Save membuang perubahan

19. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
20. Hapus centang Total User
21. Klik `[✕]`
22. Verifikasi tabel kembali ke state tersimpan terakhir (kolom Total User tampil)
23. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
24. Hapus centang Total User
25. Tekan Esc
26. Verifikasi tabel kembali ke state tersimpan terakhir (kolom Total User tampil), sama seperti klik `[✕]`

## Notes

- Modal Setup Column tidak memiliki `[Cancel]`; dibatalkan lewat `[✕]` atau Esc (bagian 9 konvensi). Langkah 23 sampai 26 menjalankan klausa "Esc memberi hasil yang sama" pada Expected TC-AC-SG-216 yang tidak memiliki langkah tersendiri di TC.
- Langkah 12 melanjutkan modal yang masih terbuka dari TC-AC-SG-214; langkah "Klik header Actions" dan "Klik Setup Column..." TC-AC-SG-215 tidak diulang.
- Konfigurasi kolom yang disimpan pada langkah 14 tidak dipulihkan dengan `[Reset to Default]`; hook `after` menghapus preferensi kolom (lihat Prerequisites).
- Temuan untuk QA:
  - TC-AC-SG-216: Expected "Esc memberi hasil yang sama" tidak memiliki langkah di kolom Langkah Uji; spec menambah langkah 23 sampai 26 berdasarkan Expected.
