---
id: TC-AC-DS-E2E-183-capability-dicabut-saat-form-terbuka
title: "Capability atau Local Registration Dicabut saat Form atau Dialog Terbuka: Aksi Ditolak dan Form Tetap Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-549
  - TC-AC-DS-550
  - TC-AC-DS-551
  - TC-AC-DS-552
coverage:
  web: automated
---

# Capability atau Local Registration Dicabut saat Form atau Dialog Terbuka: Aksi Ditolak dan Form Tetap Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Dewi Lestari, Modified By `Dewi L`): `totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Akun ganti akun (langkah 9): Full CRUD non-Total Control Principal: `manageSkuCUD_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_CUD_PASSWORD` (Pre-setup #7).
- Pelaku perubahan state lewat sesi API aktor (tidak dihitung sesi web): Principal Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1) (mengubah Local Registration Distributor PT Cakra Distribusi) dan administrator Total Control Principal kedua (Budi Kurniawan, Modified By `Budi K`): `totalControlSku2_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC2_PASSWORD` (Pre-setup #2) (mencabut capability role aktor #7). Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). SKU Distributor (#31); Brand Distributor (#28).
- Data Dinamis: SKU `REV-REG-01` (payload TC 549) tidak boleh tersimpan. Target Edit `HHR-ARC-200`, target Delete `TAG-ARC-OBJ`, dan target Bulk Delete `SEED-001`, `SEED-002` tidak boleh berubah.
- State global: Local Registration Distributor PT Cakra Distribusi dinonaktifkan (TC 549) dan capability Update lalu Delete role Full CRUD non-Total Control (#7) dicabut (TC 550 sampai 552). Pemulihan ke keadaan awal (Local Registration aktif, capability Update dan Delete ada) dilakukan lewat sesi API pelaku sebagai langkah penghubung per blok dan di hook `after`. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-549: Local Registration dicabut saat form Register terbuka

1. Klik `[+ SKU]` lalu isi SKU `REV-REG-01` (Asset TAG, Device Name `Asset TAG`, Brand `Nordik`, Model/Type `T-R1`, foto `foto-a.jpg`)
2. Dengan sesi API Principal (#1) nonaktifkan Local Registration Distributor `PT Cakra Distribusi` hingga tersimpan
3. Kembali ke sesi Distributor lalu klik `[Submit]`
4. Verifikasi muncul toast error: "Error, failed to register device SKU."
5. Verifikasi Popup Register tetap terbuka dengan input dipertahankan
6. Klik `[Clear Field]` lalu tutup popup dengan `[✕]`; ketik Search `REV-REG-01`, tekan Enter
7. Verifikasi tidak ada SKU baru: Search `REV-REG-01` menampilkan "No results found"
8. Klik `(←)` pada kotak Search; aktifkan kembali Local Registration Distributor `PT Cakra Distribusi` lewat sesi API Principal (#1) hingga tersimpan

### TC-AC-DS-550: Hak Update dicabut saat form Edit terbuka

9. Logout lalu login sebagai Full CRUD non-Total Control Principal (`manageSkuCUD_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_CUD_PASSWORD`) dan buka halaman `Settings > Device > Device SKU`
10. Ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
11. Ubah Model/Type menjadi `H-REV`
12. Dengan sesi API administrator (#2) cabut capability Update dari role aktor hingga tersimpan
13. Kembali ke sesi pertama lalu klik `[Save]`
14. Verifikasi muncul toast error: "Error, failed to update device SKU."
15. Verifikasi Popup Edit tetap terbuka dengan input dipertahankan
16. Verifikasi tidak ada perubahan tersimpan
17. Kembalikan Model/Type ke nilai tersimpan `H200`, tutup popup dengan `[✕]`, klik `(←)` pada kotak Search; pulihkan capability Update role aktor lewat sesi API administrator (#2)

### TC-AC-DS-551: Hak Delete dicabut saat dialog Delete terbuka

18. Ketik Search `TAG-ARC-OBJ`, tekan Enter, klik ⋯ pada baris `TAG-ARC-OBJ` lalu pilih `Delete`
19. Dengan sesi API administrator (#2) cabut capability Delete dari role aktor hingga tersimpan
20. Kembali ke sesi pertama lalu klik `[Delete]`
21. Verifikasi muncul toast error: "Error, failed to delete device SKU."
22. Verifikasi dialog konfirmasi tetap terbuka
23. Verifikasi SKU `TAG-ARC-OBJ` tetap ada
24. Tutup toast error
25. Klik `[Cancel]` dan klik `(←)` pada kotak Search; pulihkan capability Delete role aktor lewat sesi API administrator (#2)

### TC-AC-DS-552: Hak Delete dicabut saat dialog Bulk Delete terbuka

26. Ketik Search `SEED-00`, tekan Enter, lalu centang baris `SEED-001` dan `SEED-002`
27. Pilih Bulk Action > `Delete`
28. Dengan sesi API administrator (#2) cabut capability Delete dari role aktor hingga tersimpan
29. Kembali ke sesi pertama lalu klik `[Delete]`
30. Verifikasi muncul toast error: "Error, failed to delete device SKU."
31. Verifikasi dialog konfirmasi tetap terbuka
32. Verifikasi seleksi dipertahankan
33. Verifikasi tidak ada SKU terhapus
34. Klik `[Cancel]`, `Unselect All`, dan `(←)` pada kotak Search; pulihkan capability Delete role aktor lewat sesi API administrator (#2)

## Notes

- Pelaku kedua memakai sesi API karena hanya memicu perubahan state; hasilnya diasersi di sesi pertama (keputusan 2026-10-21 dan 2026-10-30), tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung tanpa `Verifikasi`: langkah 9 (ganti akun eksplisit ke #7; sesi dikembalikan ke akun default suite di hook `after`), Search untuk menemukan baris target (R-16, langkah 6, 10), pemulihan state dan field dirty serta penutupan popup atau dialog (langkah 8, 17, 25, 34, S-09), dan langkah 24 (menutup toast error "Error, failed to delete device SKU." sebelum blok TC-AC-DS-552 mengasersi toast identik, R-12, S-03).
- Pengecualian S-12 A-11: `HHR-ARC-200`, `TAG-ARC-OBJ`, `SEED-001`, dan `SEED-002` adalah SKU Pre-setup bernama literal tanpa suffix yang menjadi target aksi yang ditolak dan tidak boleh berubah (dinyatakan di `suite.md`).
- Temuan untuk QA:
  - TC 549 sampai 552 tidak mengatur ulang state setelah blok; pemulihan Local Registration dan capability ditambahkan sebagai langkah penghubung (disediakan lewat sesi API pelaku; mekanisme perubahan capability role tidak diuraikan TC, tanpa endpoint karangan).
  - Role aktor #7 bertipe custom Full CRUD; pencabutan capability Update lalu Delete memengaruhi role yang sama selama spec berjalan.
  - S-12: kode Data Dinamis `REV-REG-01` mengikuti TC tanpa suffix `{runId}` dan tidak pernah tersimpan (Submit ditolak); tidak tercakup A-11.
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
