---
id: TC-FA-FAAC-E2E-127-state-tabel-pindah-tab-refresh-dan-reset-menu
title: "State Tabel Asset Class: Dipertahankan Saat Pindah Tab Accounting dan Refresh, Direset Saat Menu Accounting Diklik Ulang"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-415
  - TC-FA-FAAC-416
  - TC-FA-FAAC-417
coverage:
  web: automated
---

# State Tabel Asset Class: Dipertahankan Saat Pindah Tab Accounting dan Refresh, Direset Saat Menu Accounting Diklik Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment), VEHICLES, IT-EQ (IT Equipment), MACHINERY, BLDG, STORAGE (Storage Equipment), OFFICE-NEW (Office Equipment (New)), LAND (Active) dan OFFICE-OLD (Office Equipment (Legacy), Inactive). Search `equip` mencocokkan HEAVY-EQ, IT-EQ, OFFICE-NEW, OFFICE-OLD, dan STORAGE; filter Active = Active menyisakan empat di antaranya (tanpa OFFICE-OLD). Seed disediakan tim FE/BE (lihat `suite.md`).
- Perilaku reset klik ulang menu Accounting mengikuti NC-01 (Dikonfirmasi): klik menu Accounting di sidebar membuka tab Preferences dan mereset Search, Sort, Filter, dan paginasi tabel Asset Class.
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### TC-FA-FAAC-415: State tabel dipertahankan saat pindah tab Accounting lalu kembali

1. Ketik Search `equip`, tekan Enter
2. Klik header Class Name dua kali (Z-A)
3. Klik icon Filter untuk membuka Filter Panel
4. Pilih Active = Active, klik `[Apply]`
5. Ubah ukuran halaman ke 25
6. Klik tab Chart of Accounts
7. Klik tab Asset Class
8. Verifikasi Search tetap berisi `equip`
9. Verifikasi sort Class Name Z-A tetap aktif
10. Verifikasi filter Active = Active tetap aktif
11. Verifikasi ukuran halaman tetap 25
12. Verifikasi urutan relatif antar baris contoh: STORAGE, OFFICE-NEW, IT-EQ, HEAVY-EQ (baris seed lain yang cocok `equip` dapat menyela)

### TC-FA-FAAC-416: State tabel dipertahankan saat refresh manual

13. Refresh halaman (F5)
14. Klik tab Asset Class
15. Verifikasi Search tetap berisi `equip`
16. Verifikasi sort Class Name Z-A tetap aktif
17. Verifikasi filter Active = Active tetap aktif
18. Verifikasi ukuran halaman tetap 25
19. Verifikasi urutan relatif antar baris contoh: STORAGE, OFFICE-NEW, IT-EQ, HEAVY-EQ (baris seed lain yang cocok dapat menyela)

### TC-FA-FAAC-417: Klik ulang menu Accounting di sidebar mereset Search, Sort, Filter, dan paginasi

20. Klik menu Accounting di sidebar
21. Verifikasi tab Preferences aktif setelah klik menu Accounting
22. Klik tab Asset Class
23. Verifikasi Search kosong
24. Verifikasi sort kembali Class Code A-Z
25. Verifikasi tidak ada filter
26. Verifikasi ukuran halaman 10

## Notes

- Langkah 1 sampai 5 TC-FA-FAAC-416 dan 417 identik dengan langkah TC-FA-FAAC-415 dan menghasilkan state yang sama; state dari langkah 1 sampai 5 dipakai ulang untuk ketiga TC (S-10). TC-FA-FAAC-417 diletakkan terakhir karena aksinya mereset state tersebut.
- Langkah penghubung (S-03): langkah 14 (TC-FA-FAAC-416 langkah 6 "klik tab Asset Class bila tab lain yang terbuka" ditulis deterministik sebagai klik tab Asset Class).
- Reset state sudah dilakukan langkah 20 sampai 22; tidak ada state tabel yang tersisa pada akhir spec.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan urutan relatif antar baris contoh, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
