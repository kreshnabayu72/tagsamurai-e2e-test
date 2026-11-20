---
id: TC-FA-FAAC-E2E-205-sinkron-cancel-scheduled-version-tax-depreciation-class-menghitung-ulang-opsi-tax-method
title: "Sinkronisasi Tax Depreciation Class: Membatalkan dan Membuat Versi Scheduled Menghitung Ulang Opsi Tax Method pada Asset Class"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-748
sourceRules: ["S-18", "E-FAAC-126", "FAAC-LOGIC-02m", "ST-38"]
smoke: []
dependsOn: []
trace:
  "S-18": [6, 19, 35]
  "E-FAAC-126": [6, 19, 35]
  "FAAC-LOGIC-02m": [19, 35]
  "ST-38": [6, 35]
coverage:
  web: automated
---

# Sinkronisasi Tax Depreciation Class: Membatalkan dan Membuat Versi Scheduled Menghitung Ulang Opsi Tax Method pada Asset Class

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (seed idempotent, dipulihkan fixture BE di hook `before` dan `after`): `Seed Irisan A` (Active; versi Current mengizinkan `Straight Line` dan `Declining Balance`; satu versi Scheduled sejak M+2 hanya mengizinkan `Straight Line`). Keadaan awal: `Seed Irisan A` belum dipakai Asset Class mana pun. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Jam: M = bulan berjalan menurut zona waktu General Settings client (NC-11); jam server dan jam browser tidak digeser spec ini. Bulan pada Effective From dan tooltip ditulis format `MMM yyyy`; asersi memakai M+n relatif terhadap M.
- Data Dinamis: tidak ada. Spec tidak melakukan Submit sehingga tidak ada Asset Class yang dibuat. Versi Scheduled `Seed Irisan A` dibatalkan dan dibuat kembali lewat UI modul Tax Depreciation Class (Cancel Scheduled Version dan pembuatan versi Scheduled sejak M+2 yang hanya mengizinkan `Straight Line`).
- Kemampuan teknis (disediakan tim FE/BE): hover pada opsi select (langkah 5 dan 34); alur Cancel Scheduled Version dan pembuatan versi Scheduled pada tab Tax Depreciation Class milik modul Tax Depreciation Class; fixture BE untuk seed dan pemulihan.
- State global: versi Scheduled `Seed Irisan A` dibatalkan pada langkah 12 dan dibuat kembali pada langkah 27; fixture BE memulihkannya ke keadaan awal di hook `after` bila spec berhenti di tengah. Form Create ditutup lewat breadcrumb `Asset Class` dan `[Leave]`.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps
1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`
3. Pilih Tax Depreciation Class `Seed Irisan A`
4. Buka select Tax Method
5. Arahkan kursor ke opsi `Declining Balance`
6. Verifikasi opsi `Declining Balance` Disabled dengan tooltip `Not allowed from <M+2 dalam format MMM yyyy>.`
7. Klik breadcrumb `Asset Class`
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`
10. Klik tab `Tax Depreciation Class`
11. Buka `Seed Irisan A`
12. Batalkan versi Scheduled `Seed Irisan A` lewat Cancel Scheduled Version milik modul Tax Depreciation Class hingga berhasil tersimpan
13. Tunggu aksi selesai
14. Klik tab `Asset Class`
15. Klik tombol `+ Asset Class` di toolbar tabel
16. Klik tab `Depreciation`
17. Pilih Tax Depreciation Class `Seed Irisan A`
18. Buka select Tax Method
19. Verifikasi opsi `Declining Balance` Enabled
20. Pilih Tax Method `Declining Balance`
21. Verifikasi Tax Method `Declining Balance` terpilih
22. Klik breadcrumb `Asset Class`
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`
25. Klik tab `Tax Depreciation Class`
26. Buka `Seed Irisan A`
27. Buat kembali versi Scheduled `Seed Irisan A` sejak M+2 yang hanya mengizinkan `Straight Line` lewat tab Tax Depreciation Class hingga berhasil tersimpan
28. Tunggu aksi selesai
29. Klik tab `Asset Class`
30. Klik tombol `+ Asset Class` di toolbar tabel
31. Klik tab `Depreciation`
32. Pilih Tax Depreciation Class `Seed Irisan A`
33. Buka select Tax Method
34. Arahkan kursor ke opsi `Declining Balance`
35. Verifikasi opsi `Declining Balance` Disabled dengan tooltip `Not allowed from <M+2 dalam format MMM yyyy>.`
36. Klik breadcrumb `Asset Class`
37. Verifikasi dialog `Unsaved Changes` tampil
38. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-748). Tidak ada TC hanya-BE di spec ini.
- Spec di atas 35 langkah (35 langkah terlampaui): TC-748 adalah satu alur berurutan yang membuka form Create tiga kali dengan dua perubahan state di modul Tax Depreciation Class di antaranya (batalkan lalu buat kembali versi Scheduled); membagi alur itu memutus bukti pemulihan opsi dan meninggalkan state Scheduled tak terpulihkan di spec terpisah. Tiga penutupan form dirty (S-08) menyumbang sembilan langkah.
- Langkah penghubung (S-03): langkah 10 sampai 13 dan 25 sampai 28 (berpindah ke modul Tax Depreciation Class dan kembali; "Tunggu aksi selesai" sesuai bagian 8b butir 8 karena hasil Cancel Scheduled Version dan pembuatan versi tidak diasersi langsung), serta tiga blok penutupan form dirty (S-08; TC menyebut "pilih Leave bila dialog tampil" dan dialog selalu tampil karena Tax Depreciation Class sudah dipilih).
- Langkah 6 dan 35 mengasersi tooltip saat select terbuka sebelum form ditutup (bagian 8b butir 5); langkah 19 Enabled membuktikan versi Scheduled yang dibatalkan memulihkan opsi.
- Temuan untuk QA: TC-748 tidak menyebut cara membuat versi Scheduled `Seed Irisan A` kembali pada tab Tax Depreciation Class; spec memakai deskripsi TC ("buat kembali versi Scheduled sejak M+2 yang hanya mengizinkan Straight Line") tanpa langkah rinci modul Tax Depreciation Class.
