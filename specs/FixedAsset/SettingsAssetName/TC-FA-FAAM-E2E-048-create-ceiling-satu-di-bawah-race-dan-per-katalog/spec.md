---
id: TC-FA-FAAM-E2E-048-create-ceiling-satu-di-bawah-race-dan-per-katalog
title: "Create: Ceiling Satu di Bawah (Race Tombol-Submit D-07 dan Penghitungan Per Katalog)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-159
  - TC-FA-FAAM-676
coverage:
  web: automated
---

# Create: Ceiling Satu di Bawah (Race Tombol-Submit D-07 dan Penghitungan Per Katalog)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client dengan katalog Asset Name dan Model/Type masing-masing satu di bawah ceiling (Pre-setup #19g). Email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_CEIL19G_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control client utama, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CEIL19G_PASSWORD`, `FA_CEIL19B_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Akun aktor berikutnya (ganti akun eksplisit): Total Control client dengan katalog Asset Name satu di bawah ceiling untuk race dua sesi (Pre-setup #19b, `Spectra.env.FA_CEIL19B_PASSWORD`). Email akun client khusus tidak tertulis di Pre-setup TC (disediakan tim FE).
- State global: State global: Master Data Count Limit diturunkan ke minimum lewat seed API untuk client khusus TC ini dan dipulihkan di hook `after` (H7); suite berjalan serial (`parallel: false`). Catatan `[Limit]`: nilai `[Limit]` pada teks dialog adalah batas master data aktif yang disetel seed API (minimum yang diizinkan), dibaca dari kemampuan seed API tim BE/FE.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Catalog Item {runId}-048` (tersimpan) dan `Create Min Item {runId}-048` (tidak tersimpan); Asset Name tambahan pemicu race `Race Filler {runId}-048` dibuat pelaku kedua lewat sesi API aktor.
- Kemampuan teknis: pembacaan entri teratas Changelog sebagai baseline (S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Catalog Item {runId}-048` dan `Race Filler {runId}-048`; pulihkan Master Data Count Limit kedua client khusus ke nilai awal.

## Test Steps

### TC-FA-FAAM-676: Katalog Asset Name dan Model/Type dihitung per katalog (client Pre-setup #19g)

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi field wajib: Asset Name `Catalog Item {runId}-048`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, UoM `Unit`
3. Pilih Brand `Dell` dan ketik model `Cat A` lalu Enter
4. Klik `[Submit]`
5. Verifikasi Toast `Success, asset name has been created.` tampil
6. Verifikasi Dialog `Asset Name Limit Reached` tidak tampil (katalog Asset Name belum melampaui batas)
7. Verifikasi Dialog `Model/Type Limit Reached` tidak tampil (katalog Model/Type belum melampaui batas)

### TC-FA-FAAM-159: Ceiling tercapai antara klik tombol dan Submit (client Pre-setup #19b)

8. Ganti akun: keluar (Logout), lalu login sebagai Total Control client Asset Name satu di bawah ceiling (Pre-setup #19b; email disediakan tim FE, `Spectra.env.FA_CEIL19B_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
9. Buka Changelog, catat entri teratas sebagai baseline, lalu tutup Modal Changelog
10. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
11. Isi field wajib: Asset Name `Create Min Item {runId}-048`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
12. Buat satu Asset Name `Race Filler {runId}-048` lewat sesi API aktor kedua hingga katalog mencapai ceiling dan record tersimpan
13. Klik `[Submit]`
14. Verifikasi Dialog `Asset Name Limit Reached` (D-07) tampil
15. Verifikasi Modal tetap terbuka dengan input dipertahankan
16. Klik `[OK]`
17. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)
18. Ketik Search `Create Min Item {runId}-048`, tekan Enter
19. Verifikasi Empty state `No results found` tampil (record tidak dibuat)
20. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
21. Buka Changelog
22. Verifikasi Entri teratas Changelog sama dengan baseline (tanpa log untuk record yang ditolak)
23. Tutup Modal Changelog

## Notes

- P-1: TC-FA-FAAM-159 butir "tanpa log" diasersi di spec asal dengan baseline Changelog langkah 9 karena precondition-nya adalah state berat (client dengan katalog satu di bawah ceiling dan dua sesi); S-05, S-12.
- Pelaku kedua lewat sesi API aktor (bukan konteks UI kedua), jadi `P-2` tidak dipakai; mekanisme pembuatan Asset Name pemicu ceiling disediakan tim BE/FE tanpa endpoint karangan (S-13).
- Langkah penghubung (tanpa `Verifikasi`): `[OK]` pada dialog, pemulihan form, Search nama sebagai pembuktian absence record dengan empty state sebagai anchor (bagian 8b butir 2), pencatatan baseline, dan penutupan Modal Changelog dan Search.
- Temuan untuk QA:
  - TC-FA-FAAM-159 berlabel "Manual Only (d) dua sesi paralel"; spec memicu race lewat sesi API aktor.
  - TC-FA-FAAM-159 dan 676 menyebut client khusus (Pre-setup #19b, #19g) tanpa email dan nama env akun Total Control; nama env diusulkan `FA_CEIL19B_PASSWORD`, `FA_CEIL19G_PASSWORD`.
