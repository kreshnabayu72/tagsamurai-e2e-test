---
id: TC-AC-ACC-E2E-046-create-sukses-af-normalisasi-input-pakai-ulang-dan-double-submit
title: "Create Client oleh Active-Full: Client Code Kapital, Nama Dihapus Dipakai Ulang, Trim, dan Double-Submit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-116
  - TC-AC-ACC-117
  - TC-AC-ACC-120
  - TC-AC-ACC-127
coverage:
  web: automated
---

# Create Client oleh Active-Full: Client Code Kapital, Nama Dihapus Dipakai Ulang, Trim, dan Double-Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-046@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Client Code literal `abc-12.x` (nilai TC-116); hook `before` menghapus lewat API sisa Client berkode `ABC-12.X` dari run sebelumnya.
- Hook `before` men-seed lewat API dan men-soft-delete Client `PT Dihapus Lama {runId}-046` (setara C-CRE-1) agar Company Name-nya boleh dipakai ulang (ACC-LOGIC-09.2). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Dataset Dinamis: `PT Kode Kapital {runId}-046` (Client Code `abc-12.x`), `PT Dihapus Lama {runId}-046` (dibuat ulang oleh TC-117), `  PT Trim Uji {runId}-046  ` (spasi awal dan akhir) dengan Email Default User `  trim.uji+{runId}-046@qwertysystem.net  `, `PT Ganda Satu {runId}-046`.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-116: Client Code otomatis kapital

1. Klik `[+ New Client]`
2. Isi Company Name `PT Kode Kapital {runId}-046`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Area Jakarta"
3. Ketik Client Code `abc-12.x`
4. Verifikasi field Client Code menampilkan `ABC-12.X` (bukan ditolak)
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, client has been created."
7. Ketik Search `PT Kode Kapital {runId}-046`, tekan Enter
8. Klik Company Name `PT Kode Kapital {runId}-046` untuk membuka Detail
9. Verifikasi Detail menampilkan Client Code `ABC-12.X`
10. Klik breadcrumb "Client" untuk kembali ke List

### TC-117: Company Name milik Client yang sudah dihapus dipakai ulang

11. Klik `[+ New Client]`
12. Isi Company Name `PT Dihapus Lama {runId}-046`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Area Jakarta"
13. Tunggu 1 detik
14. Verifikasi tidak ada pesan "Company name already exists"
15. Klik `[Submit]`
16. Verifikasi popup tertutup
17. Verifikasi toast sukses "Success, client has been created."
18. Ketik Search `PT Dihapus Lama {runId}-046`, tekan Enter
19. Verifikasi baris "PT Dihapus Lama {runId}-046" (Client baru, Active) tampil di sub-tab Active

### TC-120: Spasi awal dan akhir di-trim saat disimpan

20. Klik `[+ New Client]`
21. Isi Company Name `  PT Trim Uji {runId}-046  `, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name `Sari`, Last Name `Pratiwi`, Email `  trim.uji+{runId}-046@qwertysystem.net  `, dan Division sesuai Data valid Create
22. Pilih Group "Cabang Menteng" pada tree Select Group
23. Klik `[Submit]`
24. Verifikasi toast sukses "Success, client has been created."
25. Ketik Search `PT Trim Uji {runId}-046`, tekan Enter
26. Verifikasi baris "PT Trim Uji {runId}-046" tampil di List
27. Buka `⋯` baris `PT Trim Uji {runId}-046` lalu klik `Edit`
28. Verifikasi field Company Name berisi "PT Trim Uji {runId}-046" tanpa spasi di awal dan akhir
29. Verifikasi field Email Default User berisi "trim.uji+{runId}-046@qwertysystem.net" tanpa spasi di awal dan akhir
30. Klik `[✕]` di header popup

### TC-127: Double-submit hanya membuat satu Client

31. Klik `[+ New Client]`
32. Isi Company Name `PT Ganda Satu {runId}-046`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Area Jakarta"
33. Klik `[Submit]` dua kali dengan cepat
34. Verifikasi tombol `[Submit]` dan kontrol form ter-disable segera
35. Tunggu aksi selesai (popup tertutup)
36. Ketik Search `PT Ganda Satu {runId}-046`, tekan Enter
37. Verifikasi tepat satu Client "PT Ganda Satu {runId}-046" dibuat

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): Klik Company Name dan breadcrumb "Client" (TC-116) membuka Detail dan kembali ke List; `[✕]` menutup popup Edit pristine (TC-120); "Tunggu aksi selesai" sebelum Search (TC-127, butir 8b-8).
- Data literal: Client Code `abc-12.x` memakai nilai TC-116; hook `before` membersihkan sisanya (S-12, catatan pengecualian literal).
- Alasan di atas 35 langkah (sekitar 37 langkah): empat blok Create sukses dalam satu role dan satu kelas; tiap blok membuat Client sendiri dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-117 Post Condition butir b ("Hapus Client baru ... lewat row action Delete") adalah pembersihan; spec menyerahkannya ke hook `after` (soft-delete via API), bukan aksi UI.
  - TC-127 tidak menyebut verifikasi toast atau penutupan popup; spec hanya memverifikasi kontrol ter-disable dan jumlah Client.
