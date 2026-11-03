---
id: TC-AC-DS-E2E-163-defense-manipulasi-dom-field-terkunci-pada-edit
title: "Defense-in-Depth: Manipulasi DOM Field SKU, Range Type, User TAG, dan Device Name Terkunci Ditolak Seluruhnya"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-233
  - TC-AC-DS-234
  - TC-AC-DS-235
  - TC-AC-DS-236
coverage:
  web: automated
---

# Defense-in-Depth: Manipulasi DOM Field SKU, Range Type, User TAG, dan Device Name Terkunci Ditolak Seluruhnya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). SKU berstok `HHR-ARC-100` (stok 120) dan `TAG-ARC-USR` (stok 500) bersifat terkunci untuk SKU, Range Type, User TAG, dan Device Name.
- Data Dinamis: tidak ada; tidak ada perubahan yang boleh tersimpan pada SKU target (dipulihkan fixture BE bila tersimpan).
- Kemampuan teknis (disediakan tim FE/BE): manipulasi DOM lewat DevTools atau injeksi nilai pada field terkunci di Popup Edit SKU.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Tabel "Field terkunci yang diuji" (parameter tiap iterasi):

  | TC | SKU target | Field terkunci | Manipulasi DOM | Nilai paksa | Model/Type baru | Nilai tersimpan setelah form dimuat ulang |
  |---|---|---|---|---|---|---|
  | 233 | `HHR-ARC-100` | SKU | hapus atribut disabled pada field SKU | `HHR-ARC-199` | `H199` | SKU `HHR-ARC-100`, Model/Type `H100` |
  | 234 | `HHR-ARC-100` | Range Type | hapus atribut disabled pada field Range Type | pilih `Short Range` | `H198` | Range Type `Long Range`, Model/Type `H100` |
  | 235 | `TAG-ARC-USR` | User TAG | hapus atribut disabled pada checkbox `This is User TAG` | hilangkan centang | `T-197` | `This is User TAG` tercentang, Model/Type `T-USR` |
  | 236 | `HHR-ARC-100` | Device Name | hapus atribut read-only pada field Device Name | pilih `UHF Handheld Reader Pro` | `H196` | Device Name `UHF Handheld Reader`, Model/Type `H100` |

## Test Steps

### TC-AC-DS-233 sampai TC-AC-DS-236: Manipulasi DOM field terkunci pada Edit ditolak seluruhnya dengan toast gagal

1. Untuk setiap baris tabel "Field terkunci yang diuji" pada Prerequisites, lakukan langkah 2 sampai 11 dengan urutan baris 233, 234, 235, 236
2. Ketik Search SKU target, tekan Enter, klik ⋯ pada baris SKU target lalu pilih `Edit`
3. Lakukan manipulasi DOM kolom "Manipulasi DOM" lalu isi field dengan kolom "Nilai paksa"
4. Ganti Model/Type menjadi nilai kolom "Model/Type baru"
5. Klik `[Save]`
6. Verifikasi muncul toast error: "Error, failed to update device SKU."
7. Verifikasi seluruh Edit ditolak: perubahan Model/Type dan field lain tidak tersimpan
8. Verifikasi form dimuat ulang ke keadaan terkunci terbaru dengan nilai kolom "Nilai tersimpan setelah form dimuat ulang"
9. Verifikasi tidak ada teks tooltip V-14 sampai V-16 yang ditampilkan untuk penolakan ini
10. Tutup toast error
11. Tekan Esc lalu klik `(←)` pada kotak Search

## Notes

- Perulangan per baris tabel Prerequisites dipakai karena empat alur identik per field terkunci (8b butir 7); langkah 2 sampai 11 diulang empat kali (sepuluh langkah nominal, 40 langkah ekspansi, ditambah langkah 1). Spec berada di atas sekitar 35 langkah ekspansi; alasan: seluruhnya satu kelas harness (a, `K-1`) dengan alur identik dan berdiri sendiri per baris.
- `K-1`: TC kelas a (defense-in-depth) dengan Expected respons API (status respons dan state data) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-device-sku-backend.md`; langkah request langsung hanya mengasersi status respons dan state data (8b butir 1). Rujukan ID TC: 233, 234, 235, 236. Tidak ada request langsung; Expected berupa toast FE atas penolakan server (manipulasi DOM lewat browser).
- Langkah penghubung tanpa `Verifikasi`: langkah 2 memuat Search untuk menemukan baris target (R-16), langkah 10 (menutup toast error agar toast identik pada iterasi berikutnya tidak terbaca dari iterasi sebelumnya, R-12, S-03) dan langkah 11 (menutup popup dan Search agar iterasi berikutnya tidak bergantung pada iterasi sebelumnya, S-09).
- Pengecualian S-12 A-11: `HHR-ARC-100` dan `TAG-ARC-USR` adalah SKU Pre-setup bernama literal tanpa suffix yang menjadi target Edit yang ditolak; tidak ada perubahan yang boleh tersimpan, dan pemulihan dijamin fixture BE bila tersimpan (dinyatakan di `suite.md`).
- Temuan untuk QA:
  - Post Condition TC 233 sampai 236 ("Tidak ada perubahan pada SKU", "Tidak ada entri log baru") tidak punya langkah observasi di TC, sehingga tidak diasersi (S-01).
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
