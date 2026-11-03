---
id: TC-AC-ACTS-E2E-010-sort-stock-list-kelas-numerik-tanggal-dan-kolom-non-sortable
title: "Sort Stock List: Kelas Numerik, Kelas Tanggal Last Updated, dan Kolom Photo Non-Sortable"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-38
  - TC-AC-ACTS-39
  - TC-AC-ACTS-40
coverage:
  web: automated
---

# Sort Stock List: Kelas Numerik, Kelas Tanggal Last Updated, dan Kolom Photo Non-Sortable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Kolom numerik yang diuji (dipakai pengulangan langkah TC-AC-ACTS-38): `Total Registered`, `Available`, `In Use`, `Damaged/Missing`, masing-masing Ascending = nilai kecil ke besar (natural).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-38: Sort 3-state kelas numerik

1. Untuk setiap kolom numerik pada Prerequisites lakukan langkah 2 sampai 7 (empat kolom)
2. Klik header kolom numerik sekali
3. Verifikasi Urutan Ascending (↑) (nilai kecil ke besar, natural)
4. Klik header kolom numerik yang sama kedua kali
5. Verifikasi Urutan Descending (↓) terbalik dari Ascending
6. Klik header kolom numerik yang sama ketiga kali
7. Verifikasi Indikator sort hilang dan urutan kembali Last Updated Newest First (SKU tanpa aktivitas di akhir)

### TC-AC-ACTS-39: Sort 3-state kelas tanggal Last Updated

8. Klik header kolom `Last Updated` sekali
9. Verifikasi Urutan Ascending (↑) (Oldest First)
10. Klik header kolom `Last Updated` kedua kali
11. Verifikasi Urutan Descending (↓) terbalik dari Ascending
12. Klik header kolom `Last Updated` ketiga kali
13. Verifikasi Indikator sort hilang dan urutan kembali Last Updated Newest First (SKU tanpa aktivitas di akhir)

### TC-AC-ACTS-40: Kolom Photo non-sortable

14. Amati header kolom Photo
15. Verifikasi Kolom Photo tidak memiliki ikon sort
16. Catat urutan baris saat ini
17. Klik header kolom Photo
18. Verifikasi Klik header tidak mengubah urutan baris

## Notes

- Ekspansi di atas 35 langkah (18 langkah nominal; 4 kolom numerik mengulang langkah 2 sampai 7 sehingga 36 langkah): objek uji dan dataset sama (Sort Stock List); langkah yang diulang diparameterkan di Prerequisites (8b.7).
- Langkah penghubung (S-03): klik header ketiga mengembalikan urutan netral sebelum kolom berikutnya (S-09).
- Temuan untuk QA (S-15): TC-AC-ACTS-39 menyebut klik #1 Ascending = Oldest First dan klik #3 kembali ke Newest First; spec mengikuti. TC-AC-ACTS-40 tidak menyebut data uji pembanding; spec mencatat urutan baris sebelum klik.
