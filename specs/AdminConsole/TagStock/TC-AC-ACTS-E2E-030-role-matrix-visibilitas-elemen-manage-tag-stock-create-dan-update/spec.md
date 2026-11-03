---
id: TC-AC-ACTS-E2E-030-role-matrix-visibilitas-elemen-manage-tag-stock-create-dan-update
title: "Role Matrix: Visibilitas Elemen TAG > Stock oleh Pemegang Manage TAG Stock Read+Create dan Read+Update"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-118
  - TC-AC-ACTS-119
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen TAG > Stock oleh Pemegang Manage TAG Stock Read+Create dan Read+Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Manage TAG stock Read+Create`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Manage TAG stock Read+Create (#5) | `manageTagStockCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_CREATE_PASSWORD` |
| 2 | Manage TAG stock Read+Update (#6) | `manageTagStockUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_UPDATE_PASSWORD` |

Nama env baru yang harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e: `AC_TS_CREATE_PASSWORD`, `AC_TS_UPDATE_PASSWORD`.

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; SKU RFID `Fixture.tagStock.skuRfid` (#12) dengan unit Available dan unit In Use, serta Subject pending di Approvals (data Pre-setup TC).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada seeding.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Manage TAG stock Read+Create: TC-AC-ACTS-118

1. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid` di Stock List
2. Verifikasi `[Add Stock]` row action Stock List: Show
3. Verifikasi Row action `Detail` / Detail SKU: Show
4. Verifikasi Download: Show
5. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
6. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Hidden
7. Klik (⋯) pada baris unit di Tab Available
8. Verifikasi `[Delete]` row action Tab Available: Hidden
9. Verifikasi Row action `TAG Log` Tab Available: Show
10. Klik tab `In Use`, lalu klik (⋯) pada baris unit
11. Verifikasi Row action `TAG Log` Tab In Use: Show
12. Klik tab `Available`, lalu klik `[Event Log]`
13. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Show
14. Tutup modal Event Log
15. Verifikasi Menu Approvals > TAG Stock: Hidden
16. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Hidden
17. Verifikasi Row action `Review` Tab Active: Hidden
18. Verifikasi Row action `Detail` Tab History: Hidden

### Manage TAG stock Read+Update: TC-AC-ACTS-119

19. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Update (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock
20. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid` di Stock List
21. Verifikasi `[Add Stock]` row action Stock List: Hidden
22. Verifikasi Row action `Detail` / Detail SKU: Show
23. Verifikasi Download: Show
24. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
25. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Show
26. Klik (⋯) pada baris unit di Tab Available
27. Verifikasi `[Delete]` row action Tab Available: Hidden
28. Verifikasi Row action `TAG Log` Tab Available: Show
29. Klik tab `In Use`, lalu klik (⋯) pada baris unit
30. Verifikasi Row action `TAG Log` Tab In Use: Show
31. Klik tab `Available`, lalu klik `[Event Log]`
32. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Show
33. Tutup modal Event Log
34. Verifikasi Menu Approvals > TAG Stock: Hidden
35. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Hidden
36. Verifikasi Row action `Review` Tab Active: Hidden
37. Verifikasi Row action `Detail` Tab History: Hidden

## Notes

- Sekitar 35 langkah (di atas smell, 37 langkah): semua blok satu kelas (Role Matrix visibilitas) dengan dataset yang sama; setiap role wajib memuat sebelas Verifikasi (S-01) ditambah langkah navigasi menuju elemen, dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30); langkah tiap role identik tetapi hasil Show dan Hidden berbeda.
- Langkah penghubung (S-03): menutup modal Event Log, menutup Detail Approval, dan membuka tab `Available` kembali sebelum langkah berikutnya; Row action `Review` dan `Detail` Tab History hanya diamati bila menu Approvals > TAG Stock tampil, sedangkan Hidden pada menu itu berarti `[Submit]`, `Review`, dan `Detail` tidak dapat dijangkau (Table Tools dan halaman termuat menjadi anchor permukaan, 8b butir 2).
- Temuan untuk QA (S-15): TC sumber menulis Expected `Show (dalam scope)` untuk Distributor tanpa menyebut batas scope yang diasersi; spec mengasersi tampil untuk unit milik sendiri. Sebagian elemen Hidden (e, f, g) diasersi tanpa halaman karena menu Approvals Hidden; TC tidak memberi langkah observasi lain.
- TC-AC-ACTS-119: `[Audit TAG]` hanya untuk SKU RFID/NFC; spec memakai SKU RFID `Fixture.tagStock.skuRfid`.
