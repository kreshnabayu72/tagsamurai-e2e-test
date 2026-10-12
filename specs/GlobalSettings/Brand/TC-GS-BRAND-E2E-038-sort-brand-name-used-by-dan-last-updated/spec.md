---
id: TC-GS-BRAND-E2E-038-sort-brand-name-used-by-dan-last-updated
title: "Sort Tabel Brand pada Brand Name, Used By (Items), dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-146
  - TC-GS-BRAND-147
  - TC-GS-BRAND-148
  - TC-GS-BRAND-273
coverage:
  web: automated
---

# Sort Tabel Brand pada Brand Name, Used By (Items), dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession).
- Data Pre-setup (tetap di environment): 12 brand Client A dengan Last Updated sebelum hari uji; referensi Used By (Items): Orion Tech `0`, Acme Corp `1`, Northwind Co `1`, Duo Brand `2`, Kestrel `2`, Vertex Labs `5`.
- Data Dinamis: Population D-01 (12 brand: `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics`) di-seed lewat API di hook `before` (setara TC-GS-BRAND-1) dengan nama literal; total tabel 24 brand. Dihapus lewat API di hook `after`. Nama literal disengaja (asersi Search dan urutan bergantung pada nama Population; pengecualian S-12): seed idempotent (dilewati bila sudah ada), cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial.
- Data Dinamis D-39: brand `Ten Co {runId}-038` dipakai 10 Asset Name FAMS. Fixture belum ada; tim FE menyiapkan (brand + 10 Asset Name FAMS lewat API). Brand ini sengaja di-seed lewat API di tengah spec (setelah TC-GS-BRAND-147), karena TC-GS-BRAND-147 mengasumsikan Vertex Labs sebagai angka Used By tertinggi. Pembersihan di hook `after` (hapus 10 Asset Name FAMS, lalu brand), tidak berasumsi seeding berhasil penuh.
- State global: tidak ada yang diubah. Page size dan sort tabel (preferensi UI) dikembalikan ke default (10 per halaman, urutan default) di hook `after`.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: seeding fixture Asset Name FAMS lewat API di tengah spec.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-146: Sort Brand Name 3 state

2. Klik header Brand Name sekali
3. Verifikasi urutan A-Z (Acme Corp di atas)
4. Klik header Brand Name sekali lagi
5. Verifikasi urutan Z-A (Zenith Corp di atas)
6. Klik header Brand Name sekali lagi
7. Verifikasi urutan kembali ke default

### TC-GS-BRAND-148: Sort Last Updated Oldest First dan Newest First

8. Klik header Last Updated
9. Verifikasi ascending: brand Pre-setup (lama) di atas
10. Klik header Last Updated sekali lagi
11. Verifikasi descending: brand terakhir dibuat atau diubah (Population) di atas

### TC-GS-BRAND-147: Sort Used By (Items) numerik berdasarkan angka

12. Ubah page size 25
13. Klik header Used By (Items)
14. Verifikasi ascending: brand dengan `0` (mis. Orion Tech) lebih dulu, lalu `1` (Acme Corp sebelum Northwind Co, tiebreaker Brand Name A-Z), lalu `2` (Duo Brand, Kestrel), dan Vertex Labs (`5`) paling akhir; urutan numerik, bukan teks
15. Klik header Used By (Items) sekali lagi
16. Verifikasi descending: Vertex Labs di atas; brand dengan angka sama tetap Brand Name A-Z

### TC-GS-BRAND-273: Sort Used By (Items) numerik, bukan teks

17. Siapkan lewat API (fixture): brand `Ten Co {runId}-038` dipakai 10 Asset Name FAMS (D-39)
18. Muat ulang halaman agar Ten Co {runId}-038 tampil (Search, Sort, dan page size dipertahankan)
19. Ubah page size 25
20. Klik header Used By (Items) sekali lagi hingga indikator sort hilang (urutan default)
21. Klik header Used By (Items) (ascending)
22. Verifikasi ascending berurutan numerik: `2` (Duo Brand, Kestrel) sebelum `5` (Vertex Labs) sebelum `10` (Ten Co {runId}-038); urutan teks akan menaruh `10` sebelum `2`
23. Verifikasi nilai `0` paling awal pada ascending
24. Klik header Used By (Items) sekali lagi (descending)
25. Verifikasi descending kebalikannya: Ten Co {runId}-038 (`10`) berada di atas Vertex Labs (`5`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC dalam spec: 146, 148, 147, 273. TC-GS-BRAND-148 ditaruh sebelum 147 supaya dua sort yang berjalan pada page size default (Brand Name dan Last Updated) berurutan lebih dulu, dan dua sort Used By (Items) yang butuh page size 25 berdekatan sehingga Ten Co (D-39) cukup di-seed sekali di antara keduanya. Ten Co baru di-seed sesudah TC-GS-BRAND-147 selesai karena TC itu mengasumsikan Vertex Labs sebagai angka Used By tertinggi (catatan tc-brand.md).
- Langkah penghubung: langkah 18 (muat ulang halaman supaya Ten Co yang baru di-seed tampil; Search, Sort, dan page size dipertahankan) dan langkah 20 (klik header Used By (Items) hingga indikator sort hilang, supaya klik berikutnya menghasilkan ascending).
- Angka `10` pada TC-GS-BRAND-273 mengacu ke Ten Co bersuffix per run dan nomor spec (`{runId}-038`) karena nama yang sama juga dipakai spec TC-GS-BRAND-E2E-045.
- TC-GS-BRAND-146 dan TC-GS-BRAND-148 memakai Population (dependensi TC-GS-BRAND-1) yang di-seed spec ini sendiri di hook `before`.
