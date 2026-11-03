---
id: TC-FA-FAAL-E2E-066-defense-in-depth-xss-markup-dan-tulis-log-ditolak
title: "Defense-in-Depth: Payload Skrip dan SQL, Markup, dan Tulis Log Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-259
  - TC-FA-FAAL-262
  - TC-FA-FAAL-260
coverage:
  web: automated
---

# Defense-in-Depth: Payload Skrip dan SQL, Markup, dan Tulis Log Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

  | Peran dalam spec | Pre-setup | Email | Env var password |
  |---|---|---|---|
  | Total Control (Admin Alpha), client utama | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | Total Control pada client Batas Waktu | #15 | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `Spectra.env.FA_TCBATAS_PASSWORD` |
- Login akun aktor pertama (Total Control, Pre-setup #1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1, client utama).
- Kemampuan teknis disediakan tim FE: klien HTTP dengan token sesi Total Control untuk TC-FA-FAAL-262 (butir "Kemampuan teknis tambahan" di `suite.md`). Endpoint PUT dan DELETE untuk baris log tidak ditulis di TC (lihat Temuan untuk QA) dan disediakan tim BE/FE, tanpa endpoint karangan.
- Env var `FA_TC_PASSWORD` dan `FA_TCBATAS_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password dan token tidak ditulis di spec atau fixture.
- Data: Tab User Action UA-01 sampai UA-15 (Pre-setup #12, total 15 baris; UA-01 14:30 Assign / Total Control / Budi Santoso / Access Level / `—` / Total Control / Admin Alpha) dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE). Client Batas Waktu (Pre-setup #15) memuat baris BD-U6 dengan Name `<b>PT Uji</b>`, disediakan tim FE/BE.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk kedua akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nilai data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-259: Payload skrip dan SQL pada Search diperlakukan sebagai teks biasa

1. Klik tab User Action
2. Klik icon Filter
3. Pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date
4. Klik `[Apply]`
5. Ketik Search `<script>alert(1)</script>`, tekan Enter
6. Verifikasi hasil Search `<script>alert(1)</script>`: `No results found`
7. Verifikasi hasil Search `<script>alert(1)</script>`: tidak ada dialog skrip
8. Verifikasi hasil Search `<script>alert(1)</script>`: tidak ada baris tambahan
9. Ganti isi kotak search dengan `' OR 1=1 --`, tekan Enter
10. Verifikasi hasil Search `' OR 1=1 --`: `No results found`
11. Verifikasi hasil Search `' OR 1=1 --`: tidak ada dialog skrip
12. Verifikasi hasil Search `' OR 1=1 --`: tidak ada baris tambahan
13. Kosongkan isi kotak search, tekan Enter
14. Verifikasi setelah input dikosongkan: 15 baris kembali tampil (teks pagination `Showing 1–10 of 15 entries`)

### TC-FA-FAAL-262: Permintaan tulis langsung ke entri log ditolak

15. Kirim permintaan PUT mengubah New Value baris UA-01 langsung ke API dengan token sesi Total Control
16. Verifikasi respons PUT: ditolak server
17. Kirim permintaan DELETE untuk baris UA-01 langsung ke API dengan token sesi Total Control
18. Verifikasi respons DELETE: ditolak server
19. Muat ulang halaman dan klik tab User Action
20. Verifikasi UA-01 tidak berubah (14:30 Assign / Total Control / Budi Santoso / Access Level / `—` / Total Control / Admin Alpha)
21. Verifikasi jumlah baris tetap 15 (teks pagination `Showing 1–10 of 15 entries`)

### TC-FA-FAAL-260: Nilai log berisi markup dirender sebagai teks

22. Ganti akun: Logout dari akun Total Control client utama, lalu Login sebagai Total Control pada client Batas Waktu (email disediakan tim FE, password dari `Spectra.env.FA_TCBATAS_PASSWORD`) dan buka Fixed Asset > Reports & Logs > Activity Log
23. Klik tab User Action
24. Ketik Search `PT Uji`, tekan Enter
25. Verifikasi sel Name baris BD-U6 menampilkan teks literal `<b>PT Uji</b>`
26. Verifikasi sel Name baris BD-U6 tanpa cetak tebal
27. Verifikasi sel Name baris BD-U6 tanpa elemen HTML

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-FAAL-259, 260, dan 262 ada di spec ini; TC-FA-FAAL-256, 257, dan 258 ada di spec 015.
- Urutan TC di dalam spec: TC-FA-FAAL-259, 262, lalu 260. TC-FA-FAAL-260 berjalan di client Batas Waktu sehingga ditaruh terakhir agar ganti client (S-07) hanya terjadi sekali, di akhir spec.
- K-1: TC-FA-FAAL-262 adalah TC defense-in-depth dengan Expected respons API (ditolak server); tetap masuk spec FE+BE walau tumpang tindih dengan backend TC, karena TC granular tetap sumber dan tiap TC tepat satu spec. Langkah 15 sampai 18 mengirim request lewat klien HTTP, tidak melewati browser; asersi hanya penolakan dan state data (bagian 8b butir 1).
- Langkah penghubung (S-03): langkah 1 (tab User Action sebagai precondition TC), langkah 2 sampai 4 (menerapkan Filter Date Jendela Seed Tab User Action sesuai precondition d TC-FA-FAAL-259 dan 262; filter bertahan setelah muat ulang pada langkah 19), langkah 19 (muat ulang dan tab User Action untuk mengamati UA-01, TC langkah 3 "Buka Tab User Action"), langkah 22 dan 23 (ganti akun/client, lalu membuka tab), dan langkah 24 (Search `PT Uji` untuk menemukan baris BD-U6; R-16).
- Asersi absence langkah 8 dan 12 didahului anchor positif langkah 6 dan 10 (empty state `No results found` hasil Search yang sama). Langkah 13 dan 14 mengosongkan Search lalu memverifikasi baris kembali tampil.
- Langkah 20 dan 21 memverifikasi state setelah dua permintaan tulis ditolak; UA-01 dibaca pada halaman 1 (Date terbaru di atas).
- Ukuran spec 27 langkah, di bawah ambang.
- Temuan untuk QA:
  - TC-FA-FAAL-262 tidak menyebut endpoint, body, dan status respons penolakan ("ditolak server"); spec tidak mengarang endpoint (S-13) dan hanya mengasersi bahwa permintaan ditolak.
  - Pre-setup #15 tidak menyebut email dan password akun Total Control pada client Batas Waktu; spec menandainya "disediakan tim FE" dan mengusulkan env var `FA_TCBATAS_PASSWORD`.
  - TC-FA-FAAL-260 tidak menyebut cara menemukan baris BD-U6 pada tabel; spec memakai Search `PT Uji`.
  - TC-FA-FAAL-259 dan 260 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
