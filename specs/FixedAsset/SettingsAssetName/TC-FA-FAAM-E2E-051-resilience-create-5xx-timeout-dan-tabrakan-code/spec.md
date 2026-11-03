---
id: TC-FA-FAAM-E2E-051-resilience-create-5xx-timeout-dan-tabrakan-code
title: "Resilience Create: Gagal 5xx, Timeout, dan Tabrakan Code Generator"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-165
  - TC-FA-FAAM-166
  - TC-FA-FAAM-168
coverage:
  web: automated
---

# Resilience Create: Gagal 5xx, Timeout, dan Tabrakan Code Generator

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan kemampuan tabrakan Code dari tim BE/FE).
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Kemampuan teknis: `Spectra.intercept()` memaksa respons Create berstatus 500 (TC-FA-FAAM-165) dan menunda respons Create melewati timeout klien (TC-FA-FAAM-166); intercept dilepas segera setelah tiap pemicu (S-09). Untuk TC-FA-FAAM-168: kemampuan memaksa dua Create bersamaan menghasilkan kandidat Code sama dengan retry yang tetap bertabrakan (disediakan tim BE/FE tanpa endpoint karangan, S-13).
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item {runId}-051` hanya diketik dan tidak pernah tersimpan (semua Create gagal).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): lepaskan semua intercept dan kemampuan tabrakan Code; hapus lewat API Asset Name `Create Min Item {runId}-051` bila ternyata tersimpan.

## Test Steps

### TC-FA-FAAM-165: Create gagal 5xx

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi field wajib: Asset Name `Create Min Item {runId}-051`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
3. Paksa respons Create 500 lewat intercept jaringan
4. Klik `[Submit]`
5. Verifikasi Toast error `Error, failed to create asset name.` tampil
6. Hapus intercept respons 500
7. Verifikasi Modal tetap terbuka dan input dipertahankan
8. Verifikasi Tombol `[Submit]` aktif kembali untuk retry

### TC-FA-FAAM-166: Create timeout

9. Tunda respons Create melewati timeout lewat intercept jaringan
10. Klik `[Submit]`
11. Verifikasi Toast error `Connection problem. Please try again.` tampil
12. Hapus intercept penundaan
13. Verifikasi Modal tetap terbuka dan input dipertahankan
14. Verifikasi Tombol `[Submit]` aktif kembali

### TC-FA-FAAM-168: Tabrakan Code hasil generator saat commit: retry sekali lalu gagal 5xx

15. Simulasikan dua Create bersamaan yang menghasilkan kandidat Code sama dan retry tetap bertabrakan
16. Klik `[Submit]`
17. Verifikasi Toast `Error, failed to create asset name.` tampil
18. Verifikasi Modal tetap terbuka dengan input dipertahankan
19. Klik `[Submit]` lagi
20. Verifikasi Submit ulang menjalankan generator lagi (request Create baru terkirim)
21. Lepaskan kemampuan tabrakan Code
22. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)
23. Ketik Search `Create Min Item {runId}-051`, tekan Enter
24. Verifikasi Empty state `No results found` tampil (record tidak dibuat pada ketiga skenario)
25. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Form dibuka sekali dan isiannya dipertahankan oleh ketiga skenario (justru Expected TC-FA-FAAM-165, 166, dan 168 menyatakan input dipertahankan), sehingga field wajib diisi satu kali (S-10).
- Langkah "Klik `[Submit]` lagi" (langkah 19) memenuhi Expected c TC-FA-FAAM-168 ("Submit ulang menjalankan generator lagi"); TC tidak menyatakan cara mengamatinya, spec memakai pengamatan request Create baru (Temuan untuk QA).
- Mode FE+BE dengan intercept (bukan `Mode: mock`) karena asersi menyangkut state server (record tidak tersimpan) dan tabrakan Code berasal dari sisi server (bagian 6).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah pemulihan sebelum Search) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-168 ("Simulasikan dua Create bersamaan ...") tidak menyebut mekanisme; disediakan tim BE/FE tanpa endpoint karangan. Label TC "Manual Only (d) dua sesi paralel" tidak sesuai dengan spec yang memicunya dari kemampuan BE.
  - TC-FA-FAAM-168 Expected c tidak menyebut cara mengamati "generator lagi"; spec memakai pengamatan request Create baru.
