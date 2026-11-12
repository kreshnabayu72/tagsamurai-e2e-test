---
id: TC-FA-TAG-E2E-008-kartu-filter-klik-pilih-batal-dan-state-per-tab-bagian-2
title: "Kartu Filter: Gabungan dengan Search, State Independen per Tab, dan Role Read Only"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-39
  - TC-FA-TAG-40
  - TC-FA-TAG-41
coverage:
  web: automated
---

# Kartu Filter: Gabungan dengan Search, State Independen per Tab, dan Role Read Only

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit pada langkah 14 sampai 16, TC-FA-TAG-41): Read Only, `readOnly_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_RO_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite untuk kedua akun (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab Paired (hanya dibaca, tidak diubah):

  | Asset Name | Group | TAG Type | Total Assets | Reported | Non-standard | Not Paired Yet |
  |---|---|---|---|---|---|---|
  | Excavator 20 Ton | Plant A | RFID | 20 | 0 | 0 | 2 |
  | Excavator 20 Ton | Plant B | RFID | 20 | 2 | 5 | 0 |
  | Laptop Pro 14 | HQ | NFC, QR | 25 | 1 | 0 | 2 |
  | Forklift Manual | Plant A | Non TAG | 10 | 0 | 3 | 0 |

- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

### TC-FA-TAG-39: Kartu aktif digabung dengan Search

1. Klik kartu `Non-standard`
2. Ketik Search `Forklift`, tekan Enter
3. Verifikasi kartu `Non-standard` tetap aktif
4. Verifikasi tabel grup hanya memuat Forklift Manual / Plant A
5. Klik `(←)` pada kotak Search
6. Klik kartu `Non-standard` untuk membersihkan filter

### TC-FA-TAG-40: State kartu independen per tab

7. Klik kartu `Reported`
8. Klik Tab `To Be Returned`
9. Klik Tab `Paired`
10. Verifikasi kartu `Reported` masih aktif
11. Verifikasi tabel grup masih terfilter: hanya Excavator 20 Ton / Plant B dan Laptop Pro 14 / HQ
12. Verifikasi pindah tab tidak mereset state tab Paired
13. Klik kartu `Reported` untuk membersihkan filter

### TC-FA-TAG-41: Role Read Only melihat kartu filter yang sama dan dapat mengkliknya

14. Ganti akun: Logout dari akun Total Control
15. Login sebagai Read Only dengan `readOnly_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TAG_RO_PASSWORD`
16. Buka menu Fixed Asset > TAG lewat sidebar
17. Klik kartu `Reported`
18. Verifikasi kartu `Reported` aktif
19. Verifikasi tabel grup memuat Excavator 20 Ton / Plant B dan Laptop Pro 14 / HQ

## Notes

- Langkah 5, 6, 13, 14, 15, dan 16 adalah langkah penghubung (mengosongkan Search; membersihkan filter kartu; ganti akun; membuka menu), tanpa asersi (S-03, S-09).
- Langkah 14 sampai 16 adalah ganti akun eksplisit (S-07); akun pertama login di hook `before`.
- Langkah 12 adalah klausa Expected b TC-FA-TAG-40 yang merupakan kesimpulan dari langkah 10 dan 11; ditulis sebagai `Verifikasi` sendiri (S-01).
- TC-FA-TAG-31 sampai 38 ada di spec 007.
- A-15: nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena TC menuntut asersi nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-41 tidak menyebut apakah scope group Read Only sama dengan Total Control; Expected "kartu filter yang sama" dan dua grup hasil filter dipakai apa adanya.
  - TC-FA-TAG-41 Role `Read Only` berbeda dari role kapabilitas "Manage asset & TAG"; spec hanya mengasersi kartu dapat diklik.
