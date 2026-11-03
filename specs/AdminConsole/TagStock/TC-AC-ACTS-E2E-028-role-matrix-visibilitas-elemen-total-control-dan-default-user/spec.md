---
id: TC-AC-ACTS-E2E-028-role-matrix-visibilitas-elemen-total-control-dan-default-user
title: "Role Matrix: Visibilitas Elemen TAG > Stock oleh Total Control dan Default User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-114
  - TC-AC-ACTS-115
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen TAG > Stock oleh Total Control dan Default User

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Total Control`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Total Control (#1) | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| 2 | Default User (#2) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DU_PASSWORD` |

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; SKU RFID `Fixture.tagStock.skuRfid` (#12) dengan unit Available dan unit In Use, serta Subject pending di Approvals (data Pre-setup TC).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada seeding.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Total Control: TC-AC-ACTS-114

1. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid` di Stock List
2. Verifikasi `[Add Stock]` row action Stock List: Show
3. Verifikasi Row action `Detail` / Detail SKU: Show
4. Verifikasi Download: Show
5. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
6. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Show
7. Klik (⋯) pada baris unit di Tab Available
8. Verifikasi `[Delete]` row action Tab Available: Show
9. Verifikasi Row action `TAG Log` Tab Available: Show
10. Klik tab `In Use`, lalu klik (⋯) pada baris unit
11. Verifikasi Row action `TAG Log` Tab In Use: Show
12. Klik tab `Available`, lalu klik `[Event Log]`
13. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Show
14. Tutup modal Event Log
15. Klik menu sidebar Approvals > TAG Stock
16. Verifikasi Menu Approvals > TAG Stock: Show
17. Verifikasi Row action `Review` Tab Active: Show
18. Klik `Review` pada Subject pending di Tab Active
19. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Show
20. Tutup Detail Approval, lalu klik Tab History
21. Verifikasi Row action `Detail` Tab History: Show

### Default User: TC-AC-ACTS-115

22. Ganti akun: Logout, lalu login sebagai Default User (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock
23. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid` di Stock List
24. Verifikasi `[Add Stock]` row action Stock List: Show
25. Verifikasi Row action `Detail` / Detail SKU: Show
26. Verifikasi Download: Show
27. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
28. Verifikasi `[Audit TAG]` Tab Available (RFID/NFC saja): Show
29. Klik (⋯) pada baris unit di Tab Available
30. Verifikasi `[Delete]` row action Tab Available: Show
31. Verifikasi Row action `TAG Log` Tab Available: Show
32. Klik tab `In Use`, lalu klik (⋯) pada baris unit
33. Verifikasi Row action `TAG Log` Tab In Use: Show
34. Klik tab `Available`, lalu klik `[Event Log]`
35. Verifikasi `[Event Log]` dan `[Detail]` di dalam modal: Show
36. Tutup modal Event Log
37. Klik menu sidebar Approvals > TAG Stock
38. Verifikasi Menu Approvals > TAG Stock: Show
39. Verifikasi Row action `Review` Tab Active: Show
40. Klik `Review` pada Subject pending di Tab Active
41. Verifikasi `[Submit]` Approve/Reject di Detail Approval: Show
42. Tutup Detail Approval, lalu klik Tab History
43. Verifikasi Row action `Detail` Tab History: Show

## Notes

- Sekitar 35 langkah (di atas smell, 43 langkah): semua blok satu kelas (Role Matrix visibilitas) dengan dataset yang sama; setiap role wajib memuat sebelas Verifikasi (S-01) ditambah langkah navigasi menuju elemen, dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30); langkah tiap role identik dan seluruh elemen berstatus Show untuk kedua role (TC-AC-ACTS-114 dan 115).
- Langkah penghubung (S-03): menutup modal Event Log, menutup Detail Approval, dan membuka tab `Available` kembali sebelum langkah berikutnya; Row action `Review` dan `Detail` Tab History diamati setelah menu Approvals > TAG Stock tampil.
- Temuan untuk QA (S-15): TC-AC-ACTS-115 Data Uji menyebut Default User masuk approver pool (§2.3) tanpa langkah observasi UI; spec tidak mengasersi keanggotaan pool dan hanya mengasersi elemen Show pada Expected.
