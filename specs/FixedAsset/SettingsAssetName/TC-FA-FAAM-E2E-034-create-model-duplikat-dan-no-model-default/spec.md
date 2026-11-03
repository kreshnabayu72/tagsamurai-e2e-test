---
id: TC-FA-FAAM-E2E-034-create-model-duplikat-dan-no-model-default
title: "Create: Model Duplikat dalam Brand dan Badge Default No Model"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-133
  - TC-FA-FAAM-135
coverage:
  web: automated
---

# Create: Model Duplikat dalam Brand dan Badge Default No Model

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item 135 {runId}-034` (Brand `Dell` tanpa model ketikan) dibuat spec di TC-FA-FAAM-135.
- Kemampuan teknis (disediakan tim FE): pengamatan jeda 500 ms cek keunikan model; spec menunggu 600 ms nyata.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Create Min Item 135 {runId}-034` bila masih ada.

## Test Steps

### TC-FA-FAAM-133: Nama model duplikat dalam Brand yang sama ditolak

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Pilih Brand `Dell`
3. Tambahkan model `X1` (ketik, tekan Enter)
4. Ketik `X1` lagi, tunggu jeda 500 ms
5. Verifikasi Error inline `Model name already exists` tampil pada input model setelah jeda 500 ms
6. Tekan Enter
7. Verifikasi Error inline `Model name already exists` tetap tampil
8. Verifikasi Badge `X1` kedua tidak dibuat (hanya satu badge `X1` pada baris `Dell`)
9. Hapus isi input lalu ketik `X1 ` (spasi akhir), tunggu jeda 500 ms
10. Verifikasi Error inline `Model name already exists` tampil pada input model setelah jeda 500 ms
11. Tekan Enter
12. Verifikasi Error inline `Model name already exists` tetap tampil
13. Verifikasi Tidak ada badge model baru pada baris `Dell`
14. Hapus isi input lalu ketik `x1` (kapitalisasi beda), tunggu jeda 500 ms
15. Verifikasi Error inline `Model name already exists` tampil pada input model setelah jeda 500 ms
16. Tekan Enter
17. Verifikasi Error inline `Model name already exists` tetap tampil
18. Verifikasi Tidak ada badge model baru pada baris `Dell`

### TC-FA-FAAM-135: Brand tanpa model disisipi badge default No Model saat Submit

19. Klik `[Clear Field]`
20. Isi Asset Name `Create Min Item 135 {runId}-034`
21. Klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`
22. Pilih TAG Type `QR`
23. Pilih Brand `Dell` tanpa mengetik model
24. Pilih UoM `Unit`
25. Klik `[Submit]`
26. Ketik Search `Create Min Item 135 {runId}-034`, tekan Enter
27. Buka Popup Detail `Create Min Item 135 {runId}-034` dari tabel
28. Verifikasi Tab Models per Brand baris `Dell` menampilkan badge `No Model`
29. Tutup Popup Detail, lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Langkah penghubung (tanpa `Verifikasi`): Search nama pada langkah pencarian TC-FA-FAAM-135 hanya untuk menemukan baris target Detail (R-16); `[Clear Field]` membersihkan form sebelum TC-FA-FAAM-135 (badge `X1` dan input dikosongkan); penutupan Popup Detail dan Search di langkah terakhir memulihkan state tabel.
- Varian spasi akhir dan kapitalisasi beda pada TC-FA-FAAM-133 mengikuti TC: setiap varian diketik sesudah isi input dihapus, dengan `Verifikasi` untuk tiap klausa butir Expected (S-01).
- Urutan TC dalam spec: TC-FA-FAAM-133 (validasi diblokir) sebelum TC-FA-FAAM-135 (Create sukses) menurut S-10.
- Temuan untuk QA:
  - TC-FA-FAAM-135 menulis Data Uji lengkap tetapi langkah "Isi field wajib lengkap" dan Data Uji tidak menyebut Code; Code dibiarkan kosong sehingga hasil generator tidak diasersi di spec ini (diasersi di spec generator Code).
