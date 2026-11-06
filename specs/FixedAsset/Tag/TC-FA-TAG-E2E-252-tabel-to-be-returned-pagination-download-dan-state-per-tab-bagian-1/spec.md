---
id: TC-FA-TAG-E2E-252-tabel-to-be-returned-pagination-download-dan-state-per-tab-bagian-1
title: "Tabel To Be Returned: Pagination, Ganti Jumlah Baris, Nomor Halaman Tidak Valid, dan Sort pada Halaman 2 (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1018
  - TC-FA-TAG-1019
  - TC-FA-TAG-1020
  - TC-FA-TAG-1021
coverage:
  web: automated
---

# Tabel To Be Returned: Pagination, Ganti Jumlah Baris, Nomor Halaman Tidak Valid, dan Sort pada Halaman 2 (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned (kunci `Fixture.fixedAssetTag.tbr25`): 25 Tag To Be Returned dalam scope akun (kode dan atribut Tag ditentukan seeding; TC hanya menyebut jumlahnya), sehingga tabel berisi 3 halaman pada 10 baris per halaman dan 1 halaman pada 25 baris per halaman.
- Syarat urutan data untuk TC-FA-TAG-1021 (Precondition TC-FA-TAG-1021): dari 25 Tag To Be Returned di atas, TAG Code baris ke-11 pada urutan bawaan tabel (baris pertama halaman 2 pada 10 baris per halaman) berbeda dari TAG Code urutan ke-11 bila ke-25 kode diurutkan A-Z, sehingga asersi langkah 19 (TAG Code baris pertama halaman 2 berbeda dari yang dicatat pada langkah 16) bermakna setelah sort TAG Code; data urutan ini disediakan tim FE/BE lewat seeding fixture backend (kode dan atribut tidak ditentukan di spec ini).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since, serta urutan bawaan sesuai syarat TC-FA-TAG-1021) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Jumlah baris per halaman dikembalikan ke 10 pada langkah 10; sort dikembalikan ke netral pada akhir TC-FA-TAG-1021.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-1018: pagination bawaan 10 baris dan pilihan jumlah baris

1. Klik tab `To Be Returned`
2. Verifikasi halaman 1 menampilkan 10 baris
3. Buka pilihan jumlah baris per halaman
4. Verifikasi pilihan jumlah baris per halaman adalah 10, 25, 50, 100 tanpa opsi "All"
5. Tutup pilihan jumlah baris per halaman (Esc)

### TC-FA-TAG-1019: mengganti jumlah baris kembali ke halaman 1

6. Pindah ke halaman 2
7. Ganti jumlah baris per halaman menjadi 25
8. Verifikasi tabel kembali ke halaman 1
9. Verifikasi tabel menampilkan 25 baris
10. Ganti jumlah baris per halaman menjadi 10

### TC-FA-TAG-1020: input nomor halaman tidak valid diabaikan

11. Pindah ke halaman 2
12. Masukkan nomor halaman 99 lalu tekan Enter
13. Verifikasi tabel tetap di halaman 2
14. Masukkan nomor halaman 0 lalu tekan Enter
15. Verifikasi tabel tetap di halaman 2

### TC-FA-TAG-1021: mengganti sort tidak mengubah nomor halaman

16. Catat TAG Code baris pertama pada halaman 2 (urutan awal)
17. Klik ikon sort kolom "TAG Code"
18. Verifikasi tabel tetap di halaman 2
19. Verifikasi TAG Code baris pertama pada halaman 2 berbeda dari yang dicatat pada langkah 16
20. Klik ikon sort kolom "TAG Code" dua kali lagi hingga indikator netral

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1018 s.d. 1021). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1022 dan 1023 ada di spec 270 (Download tab To Be Returned) serta TC-FA-TAG-1024, 1025, 1027, 1028, dan 1029 ada di spec 253; TC-FA-TAG-1026 ada di spec lain.
- TC-FA-TAG-1020 Expected satu butir ("tetap di halaman 2 setelah kedua input"); spec memverifikasi sesudah tiap input karena input kedua dimulai dari keadaan sesudah input pertama.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 5 (menutup pilihan jumlah baris); 10 (mengembalikan jumlah baris per halaman ke 10); 20 (mengembalikan sort kolom TAG Code ke netral).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1018 s.d. 1020 tidak menyebut kode dan atribut 25 Tag To Be Returned; TC-FA-TAG-1021 hanya mensyaratkan urutan (TAG Code baris ke-11 pada urutan bawaan berbeda dari TAG Code urutan ke-11 secara A-Z, data disiapkan tim FE) tanpa menyebut kode; spec memakai jumlah dan syarat urutan itu.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
