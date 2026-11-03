---
id: TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp
title: "Create Client: Nilai Tepat di Batas Karakter Diterima dan Spasi Ujung Tidak Dihitung (Total Control)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-475
  - TC-AC-ACC-476
  - TC-AC-ACC-477
  - TC-AC-ACC-478
coverage:
  web: automated
---

# Create Client: Nilai Tepat di Batas Karakter Diterima dan Spasi Ujung Tidak Dihitung (Total Control)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-053@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis (nama bersuffix): `PT Batas Lima Belas {runId}-053` (Client Code `ABCDEFGHIJKLMNO` 15 karakter, Postal Code `123456789012345` 15 digit; Client Code literal sesuai TC, hook `before` menghapus sisa), `PT Batas Seratus Dua Puluh {runId}-053` (Company Email, Website, Fax, PIC Name, PIC Email, First Name, Last Name, Email Default User, Division, dan Position masing-masing tepat 120 karakter: Website, Fax, PIC Name, First Name, Last Name, Division, Position = 120×`A`; Company Email = 60×`c` + `@` + 42×`x` + `.qwertysystem.net`; PIC Email = 60×`p` + `@` + 42×`x` + `.qwertysystem.net`; Email Default User = local-part 60 karakter yang diakhiri suffix `+{runId}-053` + `@` + 42×`x` + `.qwertysystem.net`, total 120), `PT Alamat Tiga Ratus Enam Puluh {runId}-053` (Address 360×`A`), `PT Spasi Ujung Uji {runId}-053` (PIC Name, First Name = 120×`A` + 5 spasi di akhir; Address 360×`A` + 5 spasi di akhir; Last Name `Maharani`).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`
2. Centang checkbox "Stay on this form after submitting"

### TC-475: Client Code 15 karakter dan Postal Code 15 digit

3. Isi Company Name `PT Batas Lima Belas {runId}-053`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Client Code `ABCDEFGHIJKLMNO`, Postal Code `123456789012345`, Group "Cabang Menteng"
4. Verifikasi tidak ada pesan error pada Client Code
5. Verifikasi tidak ada pesan error pada Postal Code
6. Klik `[Submit]`
7. Verifikasi toast sukses "Success, client has been created."

### TC-476: Nilai tepat 120 karakter

8. Isi Company Name `PT Batas Seratus Dua Puluh {runId}-053`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Company Email, Website, Fax, PIC Name, PIC Email, First Name, Last Name, Email, Division, dan Position memakai nilai batas 120 karakter; Group "Cabang Menteng"
9. Verifikasi tidak ada pesan error pada Company Email, Website, Fax, PIC Name, PIC Email, First Name, Last Name, Email, Division, dan Position
10. Klik `[Submit]`
11. Verifikasi toast sukses "Success, client has been created."

### TC-477: Address 360 karakter

12. Isi Company Name `PT Alamat Tiga Ratus Enam Puluh {runId}-053`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Address 360×`A`, Group "Cabang Menteng"
13. Verifikasi tidak ada pesan error pada Address
14. Klik `[Submit]`
15. Verifikasi toast sukses "Success, client has been created."

### TC-478: Spasi ujung tidak dihitung

16. Hapus centang checkbox "Stay on this form after submitting"
17. Isi Company Name `PT Spasi Ujung Uji {runId}-053`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; PIC Name dan First Name 120×`A` + 5 spasi di akhir, Address 360×`A` + 5 spasi di akhir, Last Name `Maharani`, Group "Cabang Menteng"
18. Verifikasi PIC Name dan First Name: tidak ada pesan "Max. 120 characters"
19. Verifikasi Address: tidak ada pesan "Max. 360 characters"
20. Klik `[Submit]`
21. Verifikasi toast sukses "Success, client has been created."

### Verifikasi hasil di List

22. Ketik Search `PT Batas Lima Belas {runId}-053`, tekan Enter
23. Klik Company Name `PT Batas Lima Belas {runId}-053` untuk membuka Detail
24. Verifikasi Detail menampilkan Client Code "ABCDEFGHIJKLMNO" dan Postal Code "123456789012345"
25. Klik breadcrumb "Client" untuk kembali ke List
26. Ketik Search `PT Batas Seratus Dua Puluh {runId}-053`, tekan Enter
27. Buka `⋯` baris `PT Batas Seratus Dua Puluh {runId}-053` lalu klik `Edit`
28. Verifikasi popup Edit memuat Company Email, Website, Fax, PIC Name, PIC Email, First Name, Last Name, dan Email dengan nilai 120 karakter yang sama persis dengan Data Uji
29. Klik `[✕]` di header popup
30. Ketik Search `PT Alamat Tiga Ratus Enam Puluh {runId}-053`, tekan Enter
31. Buka `⋯` baris `PT Alamat Tiga Ratus Enam Puluh {runId}-053` lalu klik `Edit`
32. Verifikasi popup Edit memuat Address 360 karakter yang sama persis dengan Data Uji
33. Klik `[✕]` di header popup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 45 langkah): satu popup memakai Stay (prinsip 8) untuk tiga pembuatan beruntun, satu role, satu kelas (batas nilai diterima); tiap blok berdiri sendiri.
- Langkah penghubung (S-03): Search nama unik; `✕` menutup popup Edit pristine; Detail dan Edit dibuka sesudah popup Create tertutup.
- Nilai "tepat N karakter" dihitung termasuk suffix pada Email Default User (R-06).
- Temuan untuk QA:
  - TC-476 Expected butir c hanya memeriksa 8 field di popup Edit (Division dan Position tidak diperiksa); spec mengikuti TC.
  - TC-478 tidak memverifikasi nilai tersimpan; hanya tidak ada pesan batas karakter dan toast sukses.
