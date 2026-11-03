---
id: TC-AC-DC-E2E-089-floating-toggle-viewport-kecil-dan-localstorage
title: "Sidebar Category: Auto-Collapse di Bawah 1280px Tidak Menimpa Preferensi dan Default Open saat localStorage Tidak Tersedia"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-20
  - TC-AC-DC-21
coverage:
  web: automated
---

# Sidebar Category: Auto-Collapse di Bawah 1280px Tidak Menimpa Preferensi dan Default Open saat localStorage Tidak Tersedia

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Login ulang akun yang sama di jendela privat pada TC-AC-DC-21 (langkah 8) adalah ganti konteks, bukan ganti akun.
- Data Pre-setup #14 (Pohon Uji Kategori) hanya dibaca; spec tidak membuat, mengubah, atau menghapus node. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE): mengubah ukuran viewport browser (1440px dan 1100px), membaca nilai preferensi sidebar di localStorage tanpa mengubahnya, menghapus preferensi sidebar tersimpan, serta membuka jendela privat dengan localStorage diblokir. Viewport dipulihkan ke 1440px di akhir TC-AC-DC-20 dan oleh hook `after`; jendela privat ditutup di akhir TC-AC-DC-21.
- State global yang diubah dan dipulihkan: preferensi sidebar tersimpan per user dan per halaman (localStorage).
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-20: Auto-collapse di bawah 1280px tidak menimpa preferensi tersimpan

1. Atur viewport menjadi 1440px, hapus preferensi sidebar tersimpan akun aktor, lalu muat ulang halaman dengan F5 (sidebar Open pada kunjungan pertama)
2. Catat nilai preferensi sidebar di localStorage
3. Perkecil viewport menjadi 1100px
4. Verifikasi sidebar tersembunyi otomatis pada viewport di bawah 1280px
5. Verifikasi nilai preferensi sidebar di localStorage sama dengan catatan langkah 2 selama auto-collapse
6. Perbesar viewport kembali menjadi 1440px
7. Verifikasi sidebar tampil sesuai preferensi tersimpan (Open)

### TC-AC-DC-21: Sidebar jatuh ke default Open tanpa error saat localStorage tidak tersedia

8. Ganti konteks: buka jendela privat dengan localStorage diblokir, login sebagai Total Control (Pre-setup #1), lalu buka `Settings > Device > Device Name`
9. Verifikasi sidebar tampil dengan state default Open
10. Verifikasi tidak ada error di halaman
11. Klik tombol toggle
12. Verifikasi sidebar menutup
13. Klik tombol toggle
14. Verifikasi sidebar terbuka kembali
15. Tutup jendela privat dan kembali ke jendela sesi akun aktor

## Notes

- Langkah penghubung (S-03): langkah 1 mengembalikan kunjungan pertama dan viewport 1440px; langkah 6 memulihkan viewport; langkah 15 menutup konteks privat (S-09).
- Kelas harness ringan: dua TC edge case lingkungan (viewport dan localStorage) tanpa harness eksternal; keduanya objek-uji ringan dengan permukaan sama (`P-5` butir b).
- TC-AC-DC-17, 18, dan 19 (toggle, persistensi, state per halaman) ada di spec 007.
- Temuan untuk QA: (1) TC-AC-DC-21 hanya menyebut "private window" untuk memblokir localStorage; bukan semua browser memblokir localStorage di jendela privat, sehingga mekanisme pemblokiran disediakan tim FE. (2) TC-AC-DC-21 Expected b menyebut tombol toggle "tetap berfungsi untuk sesi berjalan"; spec mengasersi tutup dan buka kembali (langkah 11 sampai 14). (3) TC-AC-DC-20 Expected c menyebut nilai localStorage tanpa kunci; pembacaan nilai disediakan tim FE.
