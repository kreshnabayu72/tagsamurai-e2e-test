---
id: TC-AC-ACHS-E2E-250-state-saving-dan-klik-ganda-submit-add-stock-manual
title: "State Saving dan Klik Ganda Submit Add Stock Manual"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-98
  - TC-AC-ACHS-100
coverage:
  web: automated
---

# State Saving dan Klik Ganda Submit Add Stock Manual

## Prerequisites

- Mode: FE+BE (backend nyata dengan penahanan respons Submit; bukan resilience).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |

- Data Pre-setup: SKU `{skuFx}` (Pre-setup #16, #27).
- Data Dinamis (suffix per run): `SN-SAVE-0001-{runId}-250` (TC-100) dan `SN-DBL-0001-{runId}-250` (TC-98); keduanya disimpan pada SKU {skuFx} dan dihapus hook `after`.
- Kemampuan teknis (disediakan tim FE): menahan respons HTTP Submit Add Stock selama 3 detik (nilai delay dari TC-100) lalu melepasnya; pada TC-98 penahanan yang sama dipakai sebagai langkah penghubung supaya spinner dapat diamati. Penahanan hanya sebagai pemicu state UI, dilepas segera setelah asersi state sementara (S-09). Fixture BE yang menghapus unit bersuffix `-{runId}-250` di hook `after` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA).
- Efek pada Pre-setup: Total Registered, Available, dan Last Updated baris SKU {skuFx} berubah selama spec berjalan (SKU Pre-setup tidak dapat dimiliki spec); unit dihapus hook `after`.

## Test Steps

### TC-AC-ACHS-100: State Saving saat Submit

1. Ketik Search `{skuFx}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuFx}`
3. Klik opsi `Add Stock`
4. Ketik `SN-SAVE-0001-{runId}-250`
5. Pasang penahanan respons Submit selama 3 detik
6. Klik `[Submit]`
7. Verifikasi `[Submit]` menampilkan spinner dan disabled
8. Verifikasi textarea dinonaktifkan selama request berjalan
9. Verifikasi toast sukses "Success, unit has been added to stock." setelah respons dilepas
10. Verifikasi halaman berpindah ke Stock Detail > Tab Available SKU `{skuFx}`
11. Lepas penahanan respons Submit

### TC-AC-ACHS-98: Klik ganda cepat pada [Submit]

12. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuFx}` (form baru)
13. Ketik `SN-DBL-0001-{runId}-250`
14. Pasang penahanan respons Submit
15. Klik `[Submit]` dua kali cepat
16. Verifikasi `[Submit]` menampilkan spinner dan disabled
17. Verifikasi input dinonaktifkan
18. Tunggu toast lama hilang otomatis, lalu lepas penahanan respons Submit
19. Verifikasi hanya satu toast sukses tampil
20. Ketik Search `SN-DBL-0001-{runId}-250` pada Tab Available, tekan Enter
21. Verifikasi hasil Search menampilkan tepat satu baris `SN-DBL-0001-{runId}-250`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-98, 100). Tidak ada TC hanya-BE di spec ini.
- Urutan TC-100 sebelum TC-98 (urutan nomor dibalik) hanya karena TC-98 memakai form baru dari Tab Available sesudah redirect TC-100; keduanya berdiri sendiri. Buka form 2 kali untuk 2 kejadian Submit sukses.
- Penahanan respons hanya untuk mengamati state UI (loading, saving) dan bukan kelas b (bagian 3 prinsip 13b); langkah 14 pada TC-98 tidak ada di langkah TC dan ditambahkan sebagai langkah penghubung, karena tanpa penahanan spinner tidak dapat diamati secara deterministik (S-03).
- Langkah 20 dan 21 (Search pada Tab Available) mengamati Expected "hanya satu unit `SN-DBL-0001` tersimpan"; Search hanya menemukan baris target (R-16).
- Temuan untuk QA:
  - TC-98 Post Condition ("Satu entri Activity Log `Add Stock`") tidak punya langkah observasi dan tidak diasersi.
  - TC-98 butir a menyebut "input dinonaktifkan" tanpa menyebut elemen mana selain textarea; spec mengasersi textarea dan `[Submit]`.
  - TC-100 menyebut delay 3 detik sebagai Data Uji; nilai itu dipakai sebagai pilihan spec.
