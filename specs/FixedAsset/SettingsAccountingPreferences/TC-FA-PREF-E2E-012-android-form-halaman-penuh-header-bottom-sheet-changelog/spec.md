---
id: TC-FA-PREF-E2E-012-android-form-halaman-penuh-header-bottom-sheet-changelog
title: "Android: form halaman penuh, ikon View history di header, dialog Save Changes bottom sheet, modal Changelog card list"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-68
  - TC-FA-PREF-69
  - TC-FA-PREF-70
  - TC-FA-PREF-71
coverage:
  mobile: automated
---

# Android: form halaman penuh, ikon View history di header, dialog Save Changes bottom sheet, modal Changelog card list

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi native Android (bukan browser web); emulator atau perangkat Android dengan aplikasi mobile terpasang disediakan tim FE. Perangkat dipakai bersama, sehingga spec berjalan serial (`parallel: false`).
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di aplikasi Android di hook `before` spec ini. Pengecualian atas `suite.md`: hook `beforeEach` web suite tidak membuka layar untuk spec ini; langkah pertama membuka Tab Preferences pada aplikasi Android. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company sesuai PA-2 (nilai awal, tidak terkunci, semua setting wajib terisi); Asset Class sesuai PA-16 (dipakai sebagai precondition TC-FA-PREF-70, tidak diasersi); Changelog Preferences terisi data contoh PA-17 (9 entri; dipakai sebagai precondition TC-FA-PREF-71, tidak diasersi).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-PREF-68: Form halaman penuh, sticky footer

1. Buka Tab Preferences pada aplikasi Android
2. Scroll form dari atas ke bawah
3. Verifikasi form tampil sebagai halaman penuh dengan SectionCard bertumpuk dan field satu kolom
4. Scroll form kembali ke atas
5. Verifikasi `[Save changes]` dan `[Cancel]` berada pada sticky footer yang tetap terlihat saat scroll

### TC-FA-PREF-69: Ikon View history di header

6. Verifikasi ikon View history tampil di header halaman (bukan di bottom sheet `[⋯]`)

### TC-FA-PREF-71: Modal Changelog card list

7. Ketuk ikon View history
8. Verifikasi entri Changelog tampil sebagai card list (bukan tabel)
9. Verifikasi toolbar Search, Filter, dan Download menjadi tombol `[⋯]` dan `[🔍]`
10. Tutup modal Changelog

### TC-FA-PREF-70: Dialog Save Changes sebagai bottom sheet

11. Ubah Default Capitalization Threshold menjadi "6.000.000"
12. Ketuk `[Save changes]`
13. Verifikasi dialog "Save Changes" tampil sebagai bottom sheet (bukan dialog tengah layar)
14. Verifikasi dialog memuat tombol `[Cancel]` dan `[Save]`
15. Ketuk `[Cancel]` pada dialog "Save Changes"
16. Kembalikan Default Capitalization Threshold ke "5.000.000"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-FA-PREF-71 ditaruh sebelum TC-FA-PREF-70 supaya blok yang membuat form dirty berada di akhir (S-10, S-09).
- Langkah penghubung (S-03): "Scroll form kembali ke atas" sebelum verifikasi sticky footer; "Tutup modal Changelog"; "Ketuk `[Cancel]` pada dialog" dan "Kembalikan Default Capitalization Threshold ke "5.000.000"" setelah TC-FA-PREF-70 (pemulihan form dirty, S-09).
- Spec berjalan di aplikasi mobile saja; `coverage.web` tidak ditulis (bagian 8).
- Temuan untuk QA:
  - TC-FA-PREF-70 Post Condition a dan b ("tidak ada perubahan data Preferences tersimpan", "tidak ada entri log baru") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-FA-PREF-68 sampai 71 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
