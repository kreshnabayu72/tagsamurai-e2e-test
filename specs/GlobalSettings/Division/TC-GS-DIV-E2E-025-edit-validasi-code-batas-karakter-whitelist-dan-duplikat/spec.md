---
id: TC-GS-DIV-E2E-025-edit-validasi-code-batas-karakter-whitelist-dan-duplikat
title: "Edit Division: Validasi Code (16 Karakter, Simbol Terlarang, Duplikat, Nilai Sendiri)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-94
  - TC-GS-DIV-95
  - TC-GS-DIV-96
  - TC-GS-DIV-97
coverage:
  web: automated
---

# Edit Division: Validasi Code (16 Karakter, Simbol Terlarang, Duplikat, Nilai Sendiri)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var), lalu sesi dipakai sepanjang spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (data environment tetap, hanya dibaca sebagai nilai duplikat; tidak diubah): Division `Finance` dengan Code `FIN` (bebas relasi). Fixture belum ada; tim FE menyiapkan `fixtures/division.json` untuk identitas data ini.
- Data dinamis (seeding Division lewat API di hook `before`; target Edit milik spec ini, pengganti `Accounting` dan `Audit` pada TC sumber): `Audit {runId}-025` dengan Code `AUD25`. Code memakai nilai literal karena asersi TC-GS-DIV-97 bergantung pada hasil huruf besar dari `aud25`. Seluruh kasus berakhir pada Save yang diblokir atau tanpa Save dan form ditutup lewat `[Leave]`, sehingga Division ini tidak pernah berubah.
- Nilai input uji diketik langsung oleh langkah: `aud25` (TC-GS-DIV-97), `CODE-15-CHARS-AX` (16 karakter, TC-GS-DIV-94), `AUD#1` (TC-GS-DIV-95), dan `fin` (TC-GS-DIV-96).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API Division `Audit {runId}-025` dan Division berkode `AUD25` bila masih ada. Hook `beforeEach`: tutup dialog atau modal yang terbuka lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: mengetik 16 karakter pada Code; menunggu debounce ±500 ms; menunggu respons `POST /v2/iam/divisions/check-availability` selesai (dipakai sebelum asersi tidak ada error duplikat).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-DIV-97: Mengetik ulang Code milik sendiri tidak menampilkan error duplicate

1. Ketik Search `Audit {runId}-025`, tekan Enter
2. Buka row action baris `Audit {runId}-025` lalu klik `Edit`
3. Hapus isi Code, lalu ketik ulang `aud25`
4. Tunggu ±500 ms (debounce pengecekan keunikan)
5. Tunggu respons check-availability selesai
6. Verifikasi Code berubah menjadi `AUD25`
7. Verifikasi tidak ada error `Code already exists` terhadap record itu sendiri

### TC-GS-DIV-94: Edit Code 16 karakter diterima input dan menampilkan error inline

8. Ganti isi Code dengan 16 karakter `CODE-15-CHARS-AX`
9. Verifikasi input menerima seluruh 16 karakter
10. Verifikasi error inline `Max. 15 characters` tampil langsung saat melebihi batas
11. Klik `[Save]`
12. Verifikasi tidak ada toast sukses
13. Verifikasi Save diblokir: modal Edit tetap terbuka

### TC-GS-DIV-95: Edit Code dengan karakter di luar whitelist menampilkan error inline

14. Ganti isi Code dengan `AUD#1`
15. Verifikasi error inline `Code contains invalid characters` tampil langsung saat mengetik
16. Klik `[Save]`
17. Verifikasi tidak ada toast sukses
18. Verifikasi Save diblokir: modal Edit tetap terbuka

### TC-GS-DIV-96: Edit Code menjadi duplikat Division lain menampilkan error

19. Ganti isi Code dengan `fin`
20. Tunggu ±500 ms (debounce pengecekan keunikan)
21. Verifikasi Code berubah menjadi `FIN`
22. Verifikasi error inline `Code already exists` tampil setelah debounce
23. Klik `[Save]`
24. Verifikasi tidak ada toast sukses
25. Verifikasi Save diblokir: modal Edit tetap terbuka
26. Klik `✕` di header modal Edit
27. Verifikasi dialog `Unsaved Changes` tampil
28. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
29. Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
30. Klik `[Leave]`
31. Verifikasi Code `AUD25` pada baris `Audit {runId}-025` di tabel tidak berubah

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-94, 95, 96, 97). Mode: FE+BE. Kelas harness: validasi diblokir.
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC berbeda dari urutan nomor TC sumber: TC-GS-DIV-97 (nilai sendiri, tanpa error) lebih dulu karena form masih bersih, lalu kasus error saat mengetik (TC-94, TC-95), dan TC-96 terakhir karena form berakhir dalam keadaan dirty yang ditutup lewat `[Leave]` (prinsip 6). Seluruh TC memakai satu pembukaan modal Edit.
- Langkah 11, 16, dan 23 (klik `[Save]`) adalah penerapan prinsip 7 (tiap validasi diakhiri submit yang diblokir) pada TC-94, 95, dan 96; Langkah Uji TC sumber hanya berhenti pada mengetik. Langkah 13, 18, 25, dan 31 memeriksa bahwa tidak ada yang tersimpan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari target Edit), langkah 4 dan 20 (menunggu debounce) serta langkah 5 (menunggu respons check-availability selesai sebelum asersi tidak ada error pada langkah 7), dan langkah 26 sampai 30 (menutup form dirty lewat `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]`; teks dan tombol dialog dari TC-GS-DIV-107 dan NC-12).
- Target Edit memakai Division milik spec (`Audit {runId}-025`) sebagai pengganti `Accounting` dan `Audit` pada TC sumber. Division `Finance` Pre-setup hanya menjadi nilai duplikat dan tidak diubah.
- Temuan untuk QA:
  - TC-GS-DIV-97 menyebut nilai tersimpan `ACC` untuk `Accounting`; spec memakai nilai tersimpan `AUD25` pada Division milik spec.
  - TC-GS-DIV-94 dan TC-GS-DIV-95 tidak menyebut Save dan tidak punya Post Condition; langkah Save yang diblokir ditambahkan sesuai prinsip 7.
