---
id: TC-GS-BRAND-E2E-027-konflik-in-use-saat-confirm-delete
title: "Konflik Brand Menjadi In-Use Saat Confirm Delete"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-102
  - TC-GS-BRAND-120
  - TC-GS-BRAND-121
  - TC-GS-BRAND-122
coverage:
  web: automated
---

# Konflik Brand Menjadi In-Use Saat Confirm Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Akun admin FAMS: Admin FAMS Client A (Tari Wulandari) `famsAdmin_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.FA_ADMIN_PASSWORD`. Dipakai untuk pemicu "admin FAMS" lewat panggilan API FAMS (Create Asset Name dan Delete Asset Name) dengan sesi akun ini, tanpa sesi browser kedua. Fixture akun belum ada; tim FE menyiapkan akun ini di Client A dengan hak Create dan Delete Asset Name.
- Environment variable: `GS_TC_PASSWORD` dan `FA_ADMIN_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (seeding lewat API di hook `before`; tidak menumpang spec lain), semuanya bebas relasi saat awal kecuali disebut lain: `Fern Co {runId}-027` (D-18), `Oak Co {runId}-027` dan `Pear Co {runId}-027` (D-21), `Plum Co {runId}-027` dan `Reed Co {runId}-027` (D-22), `Sage Co {runId}-027` (dipakai 1 Asset Name FAMS `Sage Item {runId}-027` yang di-seed akun admin FAMS) dan `Teak Co {runId}-027` (D-23).
- Asset Name FAMS yang dibuat sebagai pemicu oleh akun admin FAMS: `Fern Item {runId}-027` (Brand Fern Co), `Plum Item {runId}-027` (Brand Plum Co), `Reed Item {runId}-027` (Brand Reed Co), `Pear Item {runId}-027` (Brand Pear Co). `Sage Item {runId}-027` dihapus oleh pemicu TC-GS-BRAND-122.
- Kunci fixture `fixtures/brand.json` (nilai disediakan tim FE): `famsAssetNamePayload` berisi field wajib Create Asset Name FAMS selain Asset Name dan Brand. Endpoint Create dan Delete Asset Name mengikuti kontrak FAMS; spec ini tidak menetapkan endpoint.
- Cleanup di hook `after` (tidak berasumsi seeding atau pemicu berhasil penuh): hapus dulu lewat API (akun admin FAMS) semua Asset Name FAMS di atas bila masih ada, lalu hapus brand `Fern Co`, `Oak Co`, `Pear Co`, `Plum Co`, `Reed Co`, `Sage Co`, `Teak Co` bersuffix `{runId}-027` bila masih ada.
- Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > Master Reference > Brand.
- Kemampuan teknis: panggilan API lintas modul (FAMS) sebagai akun admin FAMS di tengah spec sebagai pemicu race; membaca request daftar Brand untuk memastikan list di-refresh.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-BRAND-102: Brand menjadi in-use di antara cek awal dan Confirm

1. Buka Global Settings > Master Reference > Brand
2. Cari baris `Fern Co {runId}-027`, lalu klik `⋯` > Delete → dialog Delete Brand tampil
3. Pemicu admin FAMS: buat Asset Name `Fern Item {runId}-027` dengan Brand `Fern Co {runId}-027` (API FAMS, akun Tari Wulandari)
4. Klik [Delete]
5. Verifikasi dialog blokir in-use tampil dengan breakdown `- Fixed Asset (1 asset name)`
6. Verifikasi tidak ada toast
7. Klik [OK]
8. Verifikasi `Fern Co {runId}-027` tetap di tabel

### TC-GS-BRAND-121: Seluruh item bebas menjadi in-use sebelum Confirm (0 terhapus)

9. Search `{runId}-027`
10. Centang baris `Plum Co {runId}-027` dan `Reed Co {runId}-027`
11. Klik `Bulk Action` > `Delete` → dialog Bulk Delete tampil
12. Pemicu admin FAMS: buat Asset Name `Plum Item {runId}-027` dengan Brand `Plum Co {runId}-027` dan Asset Name `Reed Item {runId}-027` dengan Brand `Reed Co {runId}-027` (API FAMS, akun Tari Wulandari)
13. Klik [Delete]
14. Verifikasi dialog blokir tampil dengan bullet `• Plum Co {runId}-027` dan `• Reed Co {runId}-027`
15. Verifikasi tidak ada toast
16. Klik [OK]
17. Verifikasi tidak ada brand terhapus: `Plum Co {runId}-027` dan `Reed Co {runId}-027` masih ada di tabel
18. Verifikasi seleksi kedua baris dipertahankan (checkbox tercentang dan Bulk Action Bar menunjukkan 2 terpilih)
19. Verifikasi daftar di-refresh (request daftar Brand dimuat ulang)
20. Klik icon `(✕)` pada Bulk Action Bar
21. Tunggu Bulk Action Bar hilang (seleksi 0) sebelum mencentang Oak Co dan Pear Co
22. Search `{runId}-027`

### TC-GS-BRAND-120: Item bebas menjadi in-use sebelum Confirm Bulk Delete homogen

23. Centang baris `Oak Co {runId}-027` dan `Pear Co {runId}-027`
24. Klik `Bulk Action` > `Delete` → dialog Bulk Delete tampil
25. Pemicu admin FAMS: buat Asset Name `Pear Item {runId}-027` dengan Brand `Pear Co {runId}-027` (API FAMS, akun Tari Wulandari)
26. Klik [Delete]
27. Verifikasi `Oak Co {runId}-027` terhapus
28. Verifikasi `Pear Co {runId}-027` dilewati
29. Verifikasi toast sukses: "Success, brand has been deleted. Some items were skipped."

### TC-GS-BRAND-122: Brand di kelompok will be skipped tetap dilewati walau bebas saat Confirm

30. Search `{runId}-027`
31. Centang baris `Sage Co {runId}-027` dan `Teak Co {runId}-027`
32. Klik `Bulk Action` > `Delete` → dialog Bulk Delete campuran (Dialog 3, title `Delete Brands`) tampil
33. Pemicu admin FAMS: hapus Asset Name `Sage Item {runId}-027` yang memakai Brand `Sage Co {runId}-027` (API FAMS, akun Tari Wulandari)
34. Klik [Continue] pada dialog Bulk Delete campuran
35. Verifikasi `Teak Co {runId}-027` terhapus
36. Verifikasi `Sage Co {runId}-027` tetap ada di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas harness: multi-konteks (race dengan aksi admin FAMS di modul lain), bagian 3 prinsip 13c.
- Urutan TC berbeda dari urutan sourceTc: TC-102 dan TC-121 (tidak ada brand yang terhapus) dulu, lalu TC-120 dan TC-122 yang menghapus brand (prinsip 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 16 (klik [OK] untuk menutup dialog blokir; TC sumber tidak menyebutnya); langkah 20 (klik icon `(✕)` pada Bulk Action Bar mengosongkan seleksi Plum Co dan Reed Co yang dipertahankan TC-121 supaya TC-120 mulai dari seleksi kosong; tombol `Unselect All` hanya tampil saat seluruh data terseleksi, sehingga tidak dipakai); langkah 9, 22, dan 30 (Search `{runId}-027` supaya brand dinamis spec tampil sebelum dicentang). Langkah 21 memastikan prasyarat TC-120 (seleksi kosong) terpenuhi. Teks dialog Bulk Delete campuran (Dialog 3) pada langkah 32 dirujuk ke TC-GS-BRAND-117; TC-122 tidak mengasersi teksnya.
- Teks bullet dialog blokir TC-121 mengikuti format `• <nama brand>`; bagian "kedua bullet" TC sumber ditulis dengan nama bersuffix.
- Satu kelas harness (race lintas modul) dengan 36 langkah; tidak melewati batas smell.
