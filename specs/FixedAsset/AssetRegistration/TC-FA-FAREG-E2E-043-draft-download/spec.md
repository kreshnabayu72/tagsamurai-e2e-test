---
id: TC-FA-FAREG-E2E-043-draft-download
title: "Sub tab Draft: Download CSV dan XLSX"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§5#r6", "EB-DL-1@tabel-draft", "EB-DL-2@tabel-draft", "EB-DL-3@tabel-draft", "EB-FB-2@download", "EB-DL-4"]
smoke: ["EB-DL-4"]
dependsOn: []
trace:
  "EB-DL-2@tabel-draft": [6, 33]
  "EB-FB-2@download": [6, 33]
  "§5#r6": [7, 10]
  "EB-DL-1@tabel-draft": [7, 17, 22, 27]
  "EB-DL-3@tabel-draft": [7, 10]
  "EB-DL-4": [30, 34]
anchor: [2]
coverage:
  web: automated
---

# Sub tab Draft: Download CSV dan XLSX

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-043-1: 6 batch Draft dengan Group `Gudang Unduh Timur {n} {runId}` (n = 1 sampai 6), Origin `—`, Total Asset `4`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − {n} menit`.
  - DU-043-2: 6 batch Draft dengan Group `Gudang Unduh Barat {n} {runId}` (n = 1 sampai 6), Origin `—`, Total Asset `9`, Progress `20%`, Requested By `Budi S`, Last Updated `T0 − {n} jam`.
  - Rina W dan Budi S adalah pengguna aktif dengan role Manage asset & TAG pada Group batch masing-masing.
- Kondisi: ukuran halaman tabel 10 baris per halaman, sehingga kedua belas batch data uji melebihi satu halaman.

## Test Steps

### Download tanpa Search dan Filter tidak dibatasi halaman
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tabel sub tab Draft memuat baris `Gudang Unduh Timur 1 {runId}`
3. Klik `(←)` pada kotak Search
4. Klik `[Download]`
5. Pilih `Download as CSV`
6. Verifikasi tidak ada toast yang tampil setelah Download
7. Verifikasi berkas `Registration-Drafts` dengan ekstensi `.csv` terunduh dan memuat 12 baris data uji, dari `Gudang Unduh Timur 1 {runId}` sampai `Gudang Unduh Timur 6 {runId}` dan dari `Gudang Unduh Barat 1 {runId}` sampai `Gudang Unduh Barat 6 {runId}`, walaupun tabel hanya menampilkan 10 baris per halaman
8. Klik `[Download]`
9. Pilih `Download as XLSX`
10. Verifikasi berkas `Registration-Drafts` dengan ekstensi `.xlsx` terunduh

### Download mengikuti Search dan Filter
11. Ketik Search `{runId}`, tekan Enter
12. Klik ikon Filter
13. Pilih opsi `Budi S` pada field `Requested By`
14. Klik `[Apply]`
15. Klik `[Download]`
16. Pilih `Download as CSV`
17. Verifikasi berkas `Registration-Drafts` dengan ekstensi `.csv` memuat baris dari `Gudang Unduh Barat 1 {runId}` sampai `Gudang Unduh Barat 6 {runId}` dan tidak memuat baris dari `Gudang Unduh Timur 1 {runId}` sampai `Gudang Unduh Timur 6 {runId}`

### Urutan baris berkas mengikuti sort aktif
18. Klik ikon sort pada header kolom `Group`
19. Klik ikon sort pada header kolom `Group` sekali lagi
20. Klik `[Download]`
21. Pilih `Download as CSV`
22. Verifikasi urutan baris pada berkas `Registration-Drafts` dengan ekstensi `.csv` mengikuti sort `Group` turun: dari `Gudang Unduh Barat 6 {runId}` sampai `Gudang Unduh Barat 1 {runId}`

### Kolom yang disembunyikan tidak ikut berkas
23. Klik header kolom Actions `⋯`
24. Hilangkan centang `Total Asset` pada panel Column Visibility
25. Klik `[Download]`
26. Pilih `Download as CSV`
27. Verifikasi berkas `Registration-Drafts` dengan ekstensi `.csv` memuat kolom `Group`, `Origin`, `Progress`, `Requested By`, dan `Last Updated` dan tidak memuat kolom `Total Asset`
28. Centang kembali `Total Asset` pada panel Column Visibility

### Download dengan hasil nol baris
29. Ganti isi kotak search dengan `Zzqxv {runId}`, tekan Enter
30. Verifikasi tombol `[Download]` aktif walaupun tabel tidak memuat baris
31. Klik `[Download]`
32. Pilih `Download as CSV`
33. Verifikasi tidak ada toast yang tampil setelah Download
34. Verifikasi berkas `Registration-Drafts` dengan ekstensi `.csv` hanya memuat baris header kolom `Group`, `Origin`, `Total Asset`, `Progress`, `Requested By`, dan `Last Updated`
