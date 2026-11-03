---
id: TC-AC-ACTS-E2E-044-lintas-permukaan-filter-dropdown-loading-kosong-dan-stale
title: "Lintas Enam Permukaan: Filter, Dropdown Loading, No options available, dan Nilai Stale"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-87
coverage:
  web: automated
---

# Lintas Enam Permukaan: Filter, Dropdown Loading, No options available, dan Nilai Stale

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Permukaan yang diuji (tabel parameter; sedikitnya 11 baris data seed per permukaan, dengan sedikitnya dua nilai distinct pada kolom dropdown filter pertama; N total dari seeding, 8b butir 10):

| No | Permukaan | Cara membuka |
|---|---|---|
| 1 | Stock List | halaman awal TAG > Stock (dibuka hook `beforeEach`) |
| 2 | Detail SKU, Tab Available | Search SKU `RFID-ASSET-CORE-R5`, klik Device Name, Tab Available |
| 3 | Detail SKU, Tab In Use | Detail SKU `RFID-ASSET-CORE-R5`, klik Tab In Use |
| 4 | Modal Event Log (Tab Add Stock) | Detail SKU `RFID-ASSET-CORE-R5`, klik `[Event Log]` |
| 5 | Approvals > TAG Stock, Tab Active | Tutup modal Event Log (permukaan 4), lalu Sidebar Approvals > TAG Stock, Tab Active |
| 6 | Approvals > TAG Stock, Tab History | Sidebar Approvals > TAG Stock, Tab History |

- Dropdown sumber kosong: satu dropdown filter per permukaan yang sumber opsinya 0 baris (precondition "tabel sumber 0 baris"; disediakan seeding atau fixture BE, TC tidak menyebut field-nya).
- Record sumber milik spec: satu record dengan nilai opsi unik bersuffix `{runId}-044` pada dropdown filter pertama tiap permukaan, di-seed di hook `before` dan dihapus lewat sesi API aktor pada langkah pemicu (pemicu state, bukan objek asersi).
- Kemampuan teknis: menghapus record sumber milik spec (nilai opsi `{runId}-044`) lewat sesi API aktor (disediakan tim FE/BE; belum ada, lihat Temuan untuk QA).
- Kemampuan teknis tambahan: `Spectra.intercept()` untuk menahan respons opsi dropdown; tahanan dilepas pada langkah asersi dan di hook `after` bila spec gagal di tengah. Menahan respons hanya untuk mengamati state UI dan bukan fault injection.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Untuk setiap baris tabel "Permukaan yang diuji", lakukan langkah 2 sampai 18
2. Buka permukaan sesuai kolom "Cara membuka"
3. Klik icon Filter
4. Tahan respons opsi dengan intercept, buka dropdown filter pertama
5. Verifikasi skeleton atau spinner mini tampil saat opsi di-fetch
6. Lepas tahanan respons, tekan Esc untuk menutup dropdown
7. Buka dropdown yang sumber opsinya 0 baris
8. Verifikasi dropdown menampilkan `No options available`
9. Verifikasi dropdown tidak menampilkan error
10. Tekan Esc, pilih record sumber milik spec `{runId}-044` di dropdown filter pertama, klik `[Apply]`
11. Hapus record sumber itu lewat sesi API aktor hingga record terhapus
12. Tunggu aksi selesai
13. Klik `[Apply]` ulang
14. Verifikasi nilai stale record yang dihapus dibersihkan dari kriteria filter
15. Verifikasi hasil tabel mengikuti kriteria tersisa
16. Verifikasi tidak ada pesan error
17. Klik `[Clear Field]`, klik `[Apply]`
18. Klik icon Filter untuk menutup panel

## Notes

- Pengulangan per permukaan (8b butir 7): langkah 2 sampai 18 diulang untuk enam permukaan pada tabel "Permukaan yang diuji" (parameter tiap iterasi ada di tabel, tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa). Dihitung dengan ekspansi, spec ini sekitar 98 langkah.
- Alasan di atas sekitar 35 langkah (8b butir 7): satu TC memuat enam permukaan ("pada setiap permukaan") dan satu TC tetap satu spec; langkah yang diulang identik per permukaan dan iterasi berdiri sendiri.
- Penghapusan record sumber lewat sesi API aktor dan penahanan respons opsi hanya memicu state UI yang diuji (nilai stale dan skeleton), bukan objek asersi; intercept dilepas segera sesudah pemicu (S-09).
- Langkah penghubung (S-03): langkah 2 (membuka permukaan), tekan Esc, `[Clear Field]` dan `[Apply]` serta penutupan panel di akhir tiap iterasi. Modal Event Log (permukaan 4) ditutup lewat kolom «Cara membuka» permukaan 5 sebelum pindah ke sidebar Approvals (S-09).
- Temuan untuk QA: langkah 11 (hapus record sumber) membutuhkan kemampuan hapus record per permukaan lewat sesi API aktor yang tidak didefinisikan TC dan belum ada; bila tidak tersedia, klausa nilai stale tidak dapat diasersi. TC tidak menyebut dropdown mana yang bersumber tabel 0 baris maupun nama field; Expected "hasil mengikuti kriteria tersisa" tidak memberi nilai konkret, spec hanya mengasersi hasil tabel mengikuti kriteria filter tersisa (kosong setelah stale dibersihkan). Modal Event Log diuji pada Tab Add Stock.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
