---
id: TC-AC-DN-E2E-010-transisi-empty-state-sidebar
title: "Transisi Empty State Sidebar saat Device Name Terakhir pada Node Dibuat dan Dihapus"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-623
  - TC-AC-DN-622
coverage:
  web: automated
---

# Transisi Empty State Sidebar saat Device Name Terakhir pada Node Dibuat dan Dihapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Master Measurement (#13: `Unit`), dan Category leaf `Kategori Sementara` (Subcategory buatan dari `GPS`, Pre-setup #27) tanpa Device Name, disediakan lewat seed fixture BE (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis (dibuat spec ini): Device Name `Transisi Gateway {runId}-010` (Measurement `Unit`, Category `Kategori Sementara`, tanpa SKU dan tanpa unit BYO), dibuat lewat form Create di TC-AC-DN-623 dan dihapus lewat Delete di TC-AC-DN-622. Cleanup di hook `after` menghapus record itu bila masih ada (tidak berasumsi setup berhasil).
- Efek pada Pre-setup bersama: tidak ada; record milik spec menjadi target aksi tulis dan hapus (S-06). Last Modified Device Name Pre-setup tidak berubah.

## Test Steps

### TC-AC-DN-623: Membuat Device Name pada node Sidebar terpilih keluar dari empty state hasil kosong

1. Expand `TAG` lalu `GPS` pada Category Sidebar
2. Pilih node `Kategori Sementara` pada Category Sidebar
3. Verifikasi empty state Title "No results found" dan Description "Try adjusting your search or filter." tampil
4. Klik tombol `+ Device Name` pada toolbar
5. Ketik "Transisi Gateway {runId}-010" pada field Device Name
6. Klik field Measurement lalu pilih `Unit`
7. Klik field Category, expand `TAG` lalu `GPS`, pilih leaf `Kategori Sementara`
8. Klik `[Submit]`
9. Verifikasi toast sukses: "Success, device name has been created."
10. Verifikasi popup form tertutup
11. Verifikasi node `Kategori Sementara` tetap terpilih
12. Verifikasi tabel menampilkan satu baris `Transisi Gateway {runId}-010` dengan Category badge `Kategori Sementara`
13. Verifikasi empty state tidak tampil lagi

### TC-AC-DN-622: Menghapus satu-satunya Device Name pada node Sidebar terpilih berpindah ke empty state hasil kosong

14. Klik ikon aksi pada kolom Actions baris `Transisi Gateway {runId}-010`
15. Klik `Delete`
16. Klik `[Delete]` pada dialog
17. Verifikasi toast sukses: "Success, device name has been deleted."
18. Verifikasi node `Kategori Sementara` tetap terpilih pada Category Sidebar
19. Verifikasi tabel menampilkan empty state dengan Title "No results found" dan Description "Try adjusting your search or filter."
20. Verifikasi tampilan bukan empty state List kosong (tanpa teks "No device names yet")
21. Verifikasi tampilan bukan error load
22. Hapus pilihan node `Kategori Sementara` pada Category Sidebar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan menyimpang dari urutan nomor TC (S-10, bagian 3): TC-AC-DN-623 (Create) mendahului TC-AC-DN-622 (Delete) karena aksi menghapus data di akhir dan Device Name yang dibuat TC-AC-DN-623 menjadi satu-satunya Device Name pada node untuk TC-AC-DN-622.
- TC-AC-DN-622 mensyaratkan Pre-setup `Door Antenna` sebagai satu-satunya Device Name di `Kategori Sementara`; spec memakai Device Name milik spec dari TC-AC-DN-623 agar record Pre-setup tidak dihapus (S-06). Akibatnya langkah klik ikon aksi memakai nama bersuffix, dan Expected TC-AC-DN-622 tetap sama.
- Nama Dinamis bersuffix `{runId}-010` (S-12); "Transisi Gateway" pada TC-AC-DN-623 ditulis dengan suffix.
- Langkah penghubung (S-03): langkah 22 melepas pilihan Sidebar agar state bersih.
- Temuan untuk QA:
  - TC-AC-DN-622 memakai `Door Antenna` Pre-setup sebagai target Delete, padahal `Door Antenna` adalah data inti bersama (Pre-setup #16) dan tidak dikategorikan `Kategori Sementara` di tabel #16; Pre-setup #27 juga tidak menyebut `Door Antenna` sebagai isi `Kategori Sementara`.
