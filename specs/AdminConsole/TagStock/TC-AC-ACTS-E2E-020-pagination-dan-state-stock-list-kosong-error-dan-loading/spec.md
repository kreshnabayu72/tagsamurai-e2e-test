---
id: TC-AC-ACTS-E2E-020-pagination-dan-state-stock-list-kosong-error-dan-loading
title: "State Stock List: Empty State, Empty-Filtered, Error Load, dan Loading"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-67
  - TC-AC-ACTS-68
  - TC-AC-ACTS-69
  - TC-AC-ACTS-70
coverage:
  web: automated
---

# State Stock List: Empty State, Empty-Filtered, Error Load, dan Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- State kosong untuk TC-AC-ACTS-67: kondisi tanpa SKU terdaftar dibuat lewat fixture BE (disediakan tim FE/BE) dan dipulihkan di langkah penghubung sesudah asersi serta di hook `after`; Data Uji Pre-setup memuat SKU sehingga kondisi ini tidak berasal dari data bersama.
- Kemampuan teknis: intercept respons 5xx dan tahanan respons (delay jaringan) pada request daftar Stock List lewat `Spectra.intercept()` di atas backend nyata; endpoint daftar data tidak disebut TC, PRD, atau LLD dan disediakan tim FE.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-68: Empty-filtered

1. Klik icon Search, ketik `zzz-tidak-ada`, tekan Enter
2. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
3. Verifikasi Tampilan bukan tampilan error
4. Klik `(←)` pada kotak Search

### TC-AC-ACTS-70: Loading state

5. Tahan respons daftar data, lalu klik menu sidebar TAG > Stock
6. Verifikasi Komponen loading tampil selama data diambil
7. Lepaskan tahanan respons
8. Verifikasi Tabel menggantikan komponen loading

### TC-AC-ACTS-69: Error load, fetch gagal bukan empty state

9. Gagalkan request daftar data (intercept respons 5xx), klik menu sidebar TAG > Stock
10. Verifikasi Copy `Unable to load this data.` dan tombol `[Try Again]` tampil
11. Verifikasi Tampilan bukan empty state
12. Lepaskan intercept, klik `[Try Again]`
13. Verifikasi Data termuat ulang dan tabel tampil

### TC-AC-ACTS-67: Empty state genuine (state kosong di akhir spec)

14. Kosongkan seluruh SKU TAG fisik terdaftar lewat fixture BE, klik menu sidebar TAG > Stock
15. Verifikasi Illustration dengan Title `No TAG stock yet` dan Description `Registered TAG inventory and SKUs will appear here.`
16. Verifikasi Tidak ada baris data
17. Pulihkan SKU lewat fixture BE

## Notes

- Pagination Stock List (TC-AC-ACTS-66, volume 101 baris atau lebih, kelas e) ada di spec 262.
- P-5 butir b: TC-AC-ACTS-69 (kegagalan 5xx, kelas b) adalah objek-uji ringan tunggal di spec ini; TC-AC-ACTS-70 hanya menahan respons untuk mengamati loading dan bukan kelas b.
- Urutan TC: TC-AC-ACTS-70 dan 69 sebelum TC-AC-ACTS-67; TC-AC-ACTS-67 ditaruh di akhir karena mengosongkan seluruh SKU (S-10).
- Langkah penghubung (S-03): `(←)` mengosongkan Search; klik menu sidebar TAG > Stock memuat ulang daftar; melepas intercept dan tahanan respons segera setelah asersi (S-09).
- Temuan untuk QA (S-15): TC-AC-ACTS-67 mensyaratkan "belum ada SKU TAG fisik terdaftar" bertentangan dengan Precondition b yang menyebut Stock List terisi minimal 5 SKU; spec membuat kondisi kosong lewat fixture BE. TC-AC-ACTS-69 tidak menyebut endpoint yang digagalkan.
