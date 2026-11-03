---
id: TC-AC-SG-E2E-007-sidebar-group-tree-toggle-persistensi-dan-collapse-otomatis
title: "Sidebar Group Tree: Toggle Open/Collapsed, Persistensi per User, dan Collapse Otomatis di Bawah 1280px"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-22
  - TC-AC-SG-23
  - TC-AC-SG-24
coverage:
  web: automated
---

# Sidebar Group Tree: Toggle Open/Collapsed, Persistensi per User, dan Collapse Otomatis di Bawah 1280px

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group).
- State yang diubah spec: preferensi Open/Collapsed Sidebar Group Tree akun aktor (tersimpan per user, TC-AC-SG-23) dan lebar jendela browser (TC-AC-SG-24, 1440px dan 1100px).
- Kemampuan teknis: penghapusan preferensi Open/Collapsed Sidebar Group Tree akun aktor sehingga akun berstatus belum punya preferensi (Expected c TC-AC-SG-23), disediakan tim FE; mekanisme penyimpanan preferensi tidak disebut TC (lihat Temuan untuk QA). Hook `before` dan `after` spec ini menghapus preferensi itu; viewport dipulihkan ke 1440px di langkah akhir TC-AC-SG-24 dan di hook `after`.
- Data Dinamis: tidak ada; spec tidak membuat data sehingga tidak ada seeding atau suffix `{runId}-007`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global selain preferensi akun aktor di atas.

## Test Steps

### TC-AC-SG-22: Collapse dan open Sidebar Group Tree lewat tombol toggle mengambang

1. Klik tombol toggle mengambang di tepi kiri panel
2. Verifikasi panel sidebar tertutup
3. Verifikasi konten tabel melebar penuh
4. Verifikasi tombol toggle pindah ke tepi kanan layar
5. Verifikasi tombol toggle memakai ikon `◀`
6. Hover tombol toggle pada state Collapsed
7. Verifikasi tooltip tombol pada state Collapsed "Open Group Tree"
8. Klik tombol toggle lagi
9. Verifikasi panel sidebar terbuka kembali
10. Hover tombol toggle pada state Open
11. Verifikasi tooltip tombol pada state Open "Collapse Group Tree"
12. Verifikasi tombol toggle memakai ikon `▶`

### TC-AC-SG-23: State Open/Collapsed sidebar tersimpan per user dan dipulihkan setelah refresh

13. Hapus preferensi Open/Collapsed sidebar akun aktor lewat kemampuan yang disediakan tim FE
14. Muat ulang halaman dengan F5
15. Verifikasi sidebar Open pada kunjungan pertama akun tanpa preferensi tersimpan
16. Klik tombol toggle untuk meng-collapse sidebar
17. Muat ulang halaman dengan F5
18. Verifikasi sidebar tetap Collapsed setelah F5 pertama
19. Klik tombol toggle untuk membuka kembali sidebar
20. Muat ulang halaman dengan F5
21. Verifikasi sidebar tetap Open setelah F5 kedua

### TC-AC-SG-24: Sidebar collapse otomatis di bawah lebar 1280px tanpa menimpa preferensi tersimpan

22. Atur lebar jendela browser menjadi 1440px dan pastikan sidebar Open
23. Perkecil lebar jendela browser menjadi 1100px
24. Verifikasi sidebar tersembunyi otomatis pada 1100px
25. Verifikasi tombol toggle tampil sebagai jalan membuka sidebar
26. Perbesar kembali lebar jendela browser menjadi 1440px
27. Verifikasi sidebar Open mengikuti preferensi tersimpan (auto-collapse tidak menimpa preferensi)

## Notes

- Langkah penghubung (S-03, S-09): langkah 13 dan 14 (mengondisikan akun tanpa preferensi tersimpan, prasyarat Expected c TC-AC-SG-23), langkah 22 (mengatur viewport 1440px, langkah awal TC-AC-SG-24). Expected c TC-AC-SG-23 ("kunjungan pertama ... Open") diasersi lebih dulu (langkah 15) karena menjadi keadaan awal Expected a dan b (bagian 8b butir 5).
- Hook `beforeEach` suite membuka halaman untuk tiap TC; blok TC-AC-SG-22 dan TC-AC-SG-24 memakai Open sebagai keadaan awal dan berakhir Open (langkah 12 dan 27); blok TC-AC-SG-23 berakhir Open (langkah 21).
- Temuan untuk QA:
  - TC-AC-SG-24 Expected a menyebut sidebar "dapat dibuka lewat tombol toggle" tanpa langkah yang mengkliknya; spec hanya mengasersi tombol toggle tampil (langkah 25) agar klik tidak menimpa preferensi yang diuji pada langkah 27.
  - TC-AC-SG-23 Expected c ("kunjungan pertama pada akun yang belum punya preferensi tersimpan") tidak punya langkah atau precondition untuk mengosongkan preferensi, dan TC tidak menyebut tempat penyimpanan preferensi (PRD §4.2b menyebut tersimpan per user); langkah 13 memakai kemampuan "disediakan tim FE" tanpa mekanisme karangan (S-13).
  - Post Condition ketiga TC bernilai "-" sehingga tidak ada yang diasersi.
