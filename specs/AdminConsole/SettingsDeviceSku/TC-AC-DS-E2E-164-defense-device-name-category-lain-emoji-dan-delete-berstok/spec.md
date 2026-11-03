---
id: TC-AC-DS-E2E-164-defense-device-name-category-lain-emoji-dan-delete-berstok
title: "Defense-in-Depth: Device Name Category Lain pada Edit, Emoji Lolos Filter FE, dan Delete SKU Berstok lewat API"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-238
  - TC-AC-DS-527
  - TC-AC-DS-529
  - TC-AC-DS-590
coverage:
  web: automated
---

# Defense-in-Depth: Device Name Category Lain pada Edit, Emoji Lolos Filter FE, dan Delete SKU Berstok lewat API

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Selection Limit (#36).
- Data Dinamis: SKU `API-EMJ-01` (TC 527) tidak boleh tersimpan; hook `after` memastikan tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): manipulasi DOM lewat console browser atau injeksi nilai; klien HTTP untuk request langsung ke server dengan token akun #1 (sesi API aktor); ID record SKU dibaca lewat fixture BE. Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- State global: Selection Limit entitas uji diatur 100 pada Plans & Licensing > Lifecycle Settings > System Limits (nilai awal 1000) lewat kemampuan fixture BE yang disediakan tim FE/BE, sebelum blok TC 529 dan dipulihkan ke 1000 di hook `after`. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-238: Device Name dari Category lain ditolak server pada Edit

1. Ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
2. Aktifkan pilihan Device Name `Rugged Handheld Reader` (Category Barcode Handheld) lewat manipulasi DOM atau injeksi nilai
3. Klik `[Save]`
4. Verifikasi muncul toast error: "Error, failed to update device SKU."
5. Tekan Esc, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
6. Verifikasi seluruh Edit ditolak dan Device Name tersimpan tetap `UHF Handheld Reader`
7. Tekan Esc lalu klik `(←)` pada kotak Search

### TC-AC-DS-527: Emoji pada Model/Type yang lolos filter FE ditolak dengan error inline dan Submit diblok

8. Klik tombol `[+ SKU]` pada toolbar
9. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
10. Klik field Device Name lalu pilih `Asset TAG`
11. Klik field Brand lalu pilih `Arcturus`
12. Ketik `T-EMJ` pada field Model/Type
13. Ketik `API-EMJ-01` pada field SKU
14. Unggah `foto-a.jpg` pada field Photo
15. Lewat console browser, sisipkan karakter 😊 langsung ke nilai input Model/Type sehingga melewati filter keystroke dan paste (simulasi browser lama atau drag-drop), lalu picu event `input` pada field
16. Verifikasi error inline "Model/type contains invalid characters" muncul di bawah field Model/Type sebelum `[Submit]` diklik
17. Klik `[Submit]`
18. Verifikasi Popup Register SKU tetap terbuka
19. Verifikasi tidak ada toast sukses
20. Klik `[Clear Field]` lalu tutup popup dengan `[✕]`, ketik Search `API-EMJ-01`, tekan Enter
21. Verifikasi tidak ada SKU baru: Search `API-EMJ-01` menampilkan "No results found"
22. Klik `(←)` pada kotak Search

### TC-AC-DS-590: Emoji pada Model/Type yang lolos filter FE ditolak dengan error inline dan Save diblok

23. Ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
24. Lewat console browser, sisipkan karakter 😊 langsung ke nilai input Model/Type sehingga melewati filter keystroke dan paste (simulasi browser lama atau drag-drop), lalu picu event `input` pada field
25. Verifikasi error inline "Model/type contains invalid characters" muncul di bawah field Model/Type sebelum `[Save]` diklik
26. Klik `[Save]`
27. Verifikasi Popup Edit SKU tetap terbuka
28. Verifikasi tidak ada toast sukses
29. Verifikasi nilai tersimpan tidak berubah: Model/Type tetap `H200`
30. Kembalikan Model/Type ke `H200` lalu tekan Esc dan klik `(←)` pada kotak Search

### TC-AC-DS-529: Delete lewat API pada SKU berstok ditolak walau UI dibypass

31. Pastikan Selection Limit bernilai 100 pada System Limits
32. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `HHR-ARC-100` (stok 120) lewat klien HTTP dengan token `totalControlSku`
33. Verifikasi Delete SKU berstok ditolak dengan status 409 dan message `SKU is still in use`
34. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi 101 ID SKU Principal sekaligus saat Selection Limit 100 lewat klien HTTP dengan token `totalControlSku`
35. Verifikasi Delete melebihi Selection Limit ditolak dengan status 422 dengan message `Invalid Device SKU IDs` pada field `ids`
36. Muat ulang List Device SKU, ketik Search `HHR-ARC-100`, tekan Enter
37. Verifikasi `HHR-ARC-100` tetap ada pada List
38. Klik `(←)` pada kotak Search
39. Verifikasi tidak ada SKU terhapus: Pagination menampilkan 13 halaman (129 SKU Principal)

## Notes

- `K-1`: TC 529 (kelas a, Expected respons API) tetap masuk spec FE+BE; langkah request langsung hanya mengasersi status respons, message, dan state data (8b butir 1). TC 238, 527, dan 590 mengasersi perilaku FE atas manipulasi DOM di browser (bukan request langsung).
- Langkah penghubung tanpa `Verifikasi`: Search untuk menemukan baris target (R-16) di langkah 1, 20, dan 30; langkah 30 mengembalikan field dirty ke nilai tersimpan sebelum menutup popup (S-09); langkah 31 memastikan Selection Limit 100 (state global).
- Spec berada di atas sekitar 35 langkah (39 langkah); alasan: semua blok satu kelas harness (a) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition TC 238 dan 590 tidak punya langkah observasi di TC dan tidak diasersi. Langkah 5 TC 238 (Device Name tersimpan) tidak ada di TC; spec menambah langkah buka ulang Edit sebagai penghubung observasi (S-14).
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
