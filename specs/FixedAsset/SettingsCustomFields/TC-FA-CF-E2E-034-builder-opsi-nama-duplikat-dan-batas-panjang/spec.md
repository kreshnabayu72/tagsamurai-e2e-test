---
id: TC-FA-CF-E2E-034-builder-opsi-nama-duplikat-dan-batas-panjang
title: "Builder Opsi: Tambah Enter, Duplikat Case-Insensitive, dan Batas Panjang"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-108
  - TC-FA-CF-109
  - TC-FA-CF-110
  - TC-FA-CF-111
coverage:
  web: automated
---

# Builder Opsi: Tambah Enter, Duplikat Case-Insensitive, dan Batas Panjang

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- N total baris tab General = 8 diturunkan dari seeding Pre-setup #12 (8b butir 10): `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`; asersi 'tepat 8 baris' mengandaikan seluruh baris tampil dalam satu halaman.
- Kemampuan teknis: injeksi nilai langsung ke DOM input (Pre-setup #26, disediakan tim FE).
- Data dinamis: tidak ada field yang disimpan; nilai yang hanya diketik: Field Name `Dup Option {runId}-034`; opsi `Class A`, `Class B`, `Class C`, `class a`, `CLASS A`, 121 dan 120 karakter `C`.
- Jeda nyata 600 ms (TC-FA-CF-109) dibatasi di bawah 30 detik sesuai bagian 6 konvensi.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-108: Opsi ditambahkan dengan Enter dan tampil sebagai badge berurutan sesuai penambahan

1. Klik `[+ Custom Field]`
2. Pilih Data Type `Dropdown`
3. Ketik `Class A` pada input Values lalu tekan Enter
4. Ketik `Class B` pada input Values lalu tekan Enter
5. Ketik `Class C` pada input Values lalu tekan Enter
6. Verifikasi tiga badge `Class A`, `Class B`, `Class C` tampil berurutan sesuai penambahan
7. Verifikasi masing-masing badge memiliki tombol hapus `✕`
8. Verifikasi input Values kosong kembali setelah tiap Enter

#### TC-FA-CF-109: Nama opsi duplikat case-insensitive ditolak setelah jeda sekitar 500 ms saat mengetik

9. Klik `[Clear Field]`
10. Pilih Data Type `Dropdown`
11. Ketik `Class A` pada input Values lalu tekan Enter
12. Ketik `class a` pada input Values tanpa menekan Enter
13. Verifikasi belum ada pesan sebelum 500 ms
14. Tunggu 600 ms
15. Verifikasi pesan inline `Option name already exists` tampil
16. Verifikasi pesan tampil tanpa menunggu kursor keluar dari input (fokus masih di input Values)

#### TC-FA-CF-110: Submit dengan opsi duplikat case-insensitive ditolak

17. Klik `[Clear Field]`
18. Pilih Data Type `Dropdown`
19. Isi Field Name `Dup Option {runId}-034`
20. Ketik `Class A` pada input Values lalu tekan Enter
21. Injeksi opsi kedua `CLASS A` melewati validasi klien
22. Klik `[Submit]`
23. Verifikasi pesan inline `Option name already exists` tampil pada Values

#### TC-FA-CF-111: Nama opsi tepat 120 karakter diterima dan 121 karakter menampilkan pesan batas

24. Klik `[Clear Field]`
25. Pilih Data Type `Dropdown`
26. Ketik opsi 121 karakter (huruf `C` diulang 121 kali)
27. Verifikasi pesan inline `Max. 120 characters` tampil langsung
28. Hapus satu karakter sehingga opsi 120 karakter
29. Verifikasi pesan inline `Max. 120 characters` tidak tampil
30. Tekan Enter
31. Verifikasi opsi 120 karakter ditambahkan sebagai badge
32. Klik `[✕]`
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`
35. Verifikasi tabel tab General memuat 8 baris (TC-FA-CF-110 butir b: field tidak tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus (halaman yang sama dipakai berulang) dan penutupan form dirty pada langkah 32 dan dua langkah berikutnya (S-08).
- Field Dinamis bernama bersuffix `{runId}-034` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- P-5: TC-FA-CF-110 (opsi duplikat lolos validasi klien lewat injeksi) adalah satu TC objek-uji ringan kelas a tanpa harness eksternal dan tanpa state berat, ditaruh di spec fungsional builder opsi yang permukaannya sama (P-5 butir b).
- Asersi 'Field tidak tersimpan' pada TC-FA-CF-110 memakai jumlah baris tab General (8, seed Pre-setup #12) setelah form ditutup.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
  - TC-FA-CF-109 butir a ('Sebelum 500 ms belum ada pesan') ditulis sebagai `Verifikasi` segera setelah mengetik, sebelum langkah Tunggu 600 ms (8b butir 5).
