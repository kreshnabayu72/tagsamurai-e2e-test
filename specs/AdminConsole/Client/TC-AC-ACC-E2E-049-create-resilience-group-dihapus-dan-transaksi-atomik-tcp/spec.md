---
id: TC-AC-ACC-E2E-049-create-resilience-group-dihapus-dan-transaksi-atomik-tcp
title: "Create Client: Group Dihapus Sebelum Submit dan Transaksi Atomik Gagal (Total Control)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-130
  - TC-AC-ACC-507
coverage:
  web: automated
---

# Create Client: Group Dihapus Sebelum Submit dan Transaksi Atomik Gagal (Total Control)

## Prerequisites

- Mode: FE+BE dengan pemicu kegagalan sisi server.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-049@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset: Group sementara `Cabang Uji Hapus {runId}-049` di bawah Area Jakarta (di-seed lewat API di hook `before`, dihapus oleh pelaku kedua pada TC-130; hook `after` menghapus sisanya). Pelaku kedua memakai sesi API (bukan sesi UI kedua). Dataset Dinamis: `PT Group Hapus Uji {runId}-049`, `PT Atomik Uji {runId}-049`.
- Kemampuan teknis (TC-507): memaksa pembuatan Default User di Global Settings gagal (5xx) lalu dipulihkan; mekanisme tidak disebut TC, disediakan tim FE/BE. Kemampuan membaca Changelog dengan Search nama unik.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-130: Group dihapus sesi lain sebelum Submit

1. Klik `[+ New Client]`
2. Isi Company Name `PT Group Hapus Uji {runId}-049`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; kosongkan Partner dan pilih Group "Cabang Uji Hapus {runId}-049" pada tree Select Group
3. Pelaku kedua (sesi API) menghapus Group "Cabang Uji Hapus {runId}-049" hingga terhapus
4. Tunggu aksi selesai
5. Klik `[Submit]`
6. Verifikasi pesan error "This group no longer exists. Please select another."
7. Verifikasi pilihan Group dikosongkan dan opsi tree dimuat ulang tanpa "Cabang Uji Hapus {runId}-049"
8. Verifikasi field lain tetap terisi (Company Name "PT Group Hapus Uji {runId}-049")
9. Klik `[✕]` di header popup
10. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
11. Klik `[Leave]`
12. Ketik Search `PT Group Hapus Uji {runId}-049`, tekan Enter
13. Verifikasi tidak ada Client "PT Group Hapus Uji {runId}-049" yang dibuat (empty state "No results found")

### TC-507: Create gagal di tengah transaksi

14. Klik `[+ New Client]`
15. Isi Company Name `PT Atomik Uji {runId}-049`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Cabang Menteng"
16. Paksa pembuatan Default User di Global Settings gagal (5xx)
17. Klik `[Submit]`
18. Verifikasi toast error "Error, failed to create client."
19. Verifikasi popup tetap terbuka dan seluruh input dipertahankan
20. Pulihkan Global Settings (respons berhasil)
21. Klik `[Submit]` lagi tanpa mengubah isian
22. Verifikasi toast sukses "Success, client has been created."
23. Verifikasi tidak ada pesan "Company name already exists"
24. Ketik Search `PT Atomik Uji {runId}-049`, tekan Enter
25. Verifikasi List sub-tab Active memuat tepat satu baris "PT Atomik Uji {runId}-049"
26. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Atomik Uji {runId}-049`, tekan Enter
27. Verifikasi Changelog memuat tepat satu baris Action `Create`, Client Name "PT Atomik Uji {runId}-049", Field `Company Name`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Pelaku kedua TC-130 memakai sesi API hingga Group terhapus (R-20); bukan konteks UI kedua, sehingga tidak butuh butir `P-2`.
- Langkah penghubung (S-03): "Tunggu aksi selesai" sesudah aksi pelaku kedua (butir 8b-8); Search nama unik; penutup form dirty (S-08).
- Temuan untuk QA:
  - TC-507 Expected butir b: pesan "Company name already exists" tidak boleh muncul, tetapi TC tidak menyebut kapan diperiksa; spec memverifikasi sesudah retry berhasil.
  - TC-507 mengandalkan "mock response 5xx" pada Global Settings yang berada di sisi server; mekanismenya disediakan tim FE/BE.
