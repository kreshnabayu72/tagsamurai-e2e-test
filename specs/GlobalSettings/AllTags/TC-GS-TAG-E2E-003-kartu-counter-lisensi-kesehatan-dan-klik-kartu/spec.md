---
id: TC-GS-TAG-E2E-003-kartu-counter-lisensi-kesehatan-dan-klik-kartu
title: "Kartu Counter: License Counter Tab All, Health Counter Tab Not Paired, Tab Paired Tanpa Kartu, dan Klik Kartu Menyetel Filter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-12
  - TC-GS-TAG-14
  - TC-GS-TAG-15
  - TC-GS-TAG-16
  - TC-GS-TAG-17
coverage:
  web: automated
---

# Kartu Counter: License Counter Tab All, Health Counter Tab Not Paired, Tab Paired Tanpa Kartu, dan Klik Kartu Menyetel Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Seed Registri A utuh (DD-01 s.d. DD-30) dengan kuota Client A: RFID–Object 50, RFID–User 20, NFC 30, BLE 30, GPS 30. Hitungan kartu (`21 of 50`, `1 of 20`, `3 of 30`, `1 of 30`, `1 of 30`, serta Health Counter 18/1/1/0/1) valid hanya pada Seed Registri A utuh; seed di-seed ulang idempotent oleh hook `before` (mekanisme disediakan tim FE/BE, Q-4). Tag Retired (DD-08) tidak dihitung; Waiting for Approval (DD-03) dihitung.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah selain state Search dan Filter tampilan (dibersihkan lewat langkah penghubung). Suite berjalan serial (`parallel: false`).
- Selektor: kartu counter individual belum punya ID/aria-label di sumber (hanya target Guided Tooltip `#license-counter-cards`); diselesaikan tim FE di tahap script.

## Test Steps

### TC-GS-TAG-12: License Counter Card Tab All menampilkan terpakai of kuota dan sisa untuk lima tipe

1. Amati lima kartu pada Tab All
2. Verifikasi kartu RFID – Object TAG `21 of 50` dengan `29 remaining`
3. Verifikasi kartu RFID – User TAG `1 of 20` dengan `19 remaining`
4. Verifikasi kartu NFC `3 of 30` dengan `27 remaining`
5. Verifikasi kartu BLE `1 of 30` dengan `29 remaining`
6. Verifikasi kartu GPS `1 of 30` dengan `29 remaining`
7. Verifikasi tag DD-08 (Retired, RFID Object) tidak dihitung pada kartu RFID – Object TAG
8. Verifikasi tidak ada kartu QR

### TC-GS-TAG-16: Klik kartu menyetel filter TAG Type dan Type; hanya satu kartu aktif

9. Klik kartu `RFID – Object TAG`
10. Buka Filter Panel dan amati field `TAG Type` dan `Type`
11. Verifikasi filter `TAG Type` = RFID
12. Verifikasi filter `Type` = Object TAG
13. Verifikasi kartu `RFID – Object TAG` diberi penanda terpilih
14. Verifikasi sedikitnya satu baris tabel tampil
15. Verifikasi baris tabel hanya RFID Object TAG
16. Verifikasi ikon Filter menampilkan titik indikator
17. Klik kartu `NFC`
18. Amati Filter Panel dan baris tabel
19. Verifikasi filter `Type` dikosongkan
20. Verifikasi filter `TAG Type` = NFC
21. Verifikasi kartu `RFID – Object TAG` tidak lagi terpilih
22. Verifikasi kartu `NFC` terpilih
23. Verifikasi baris tabel hanya NFC (`04A224B2C15E80`, `04A224B2C15E82`, `04A224B2C15E83`)
24. Verifikasi ikon Filter menampilkan titik indikator
25. Klik kartu `NFC` sekali lagi untuk membersihkan filter kartu

### TC-GS-TAG-17: Klik kartu yang sama lagi membersihkan filter kartu; filter Filter Panel tertimpa kartu

26. Buka Filter Panel, pilih `Source` = Official dan `TAG Type` = BLE, klik `Apply`
27. Klik kartu `GPS`
28. Amati nilai filter `TAG Type`
29. Verifikasi `TAG Type` = GPS (nilai BLE tertimpa)
30. Verifikasi field `Source` = Official tidak berubah
31. Klik kartu `GPS` sekali lagi
32. Verifikasi filter `TAG Type` yang disetel kartu dibersihkan
33. Verifikasi kartu `GPS` tidak lagi bertanda terpilih
34. Kosongkan seluruh field Filter Panel (`Source` dan `TAG Type`), klik `Apply` (langkah penghubung pembersih)

### TC-GS-TAG-15: Tab Paired tidak menampilkan kartu counter

35. Klik Tab Paired
36. Amati area di atas toolbar
37. Verifikasi tidak ada License Counter Card di Tab Paired
38. Verifikasi tidak ada Health Counter Card di Tab Paired

### TC-GS-TAG-14: Health Counter Card Tab Not Paired menampilkan jumlah Available dan Damaged/Missing per tipe

39. Klik Tab Not Paired
40. Amati lima kartu pada Tab Not Paired
41. Verifikasi kartu RFID – Object TAG nilai utama `18` dengan `Damaged/Missing: 0`
42. Verifikasi kartu RFID – User TAG `1` dengan `Damaged/Missing: 0`
43. Verifikasi kartu NFC `1` dengan `Damaged/Missing: 0`
44. Verifikasi kartu BLE `0` dengan `Damaged/Missing: 1`
45. Verifikasi kartu GPS `1` dengan `Damaged/Missing: 0`
46. Ketik Search `alien`, tekan Enter
47. Verifikasi sedikitnya satu baris tabel tampil
48. Verifikasi nilai kelima kartu tetap sama setelah Search
49. Klik `(←)` pada kotak Search
50. Buka Filter Panel, pilih `Source` = Self-Purchased, klik `Apply`
51. Verifikasi sedikitnya satu baris tabel tampil
52. Verifikasi nilai kelima kartu tetap sama setelah Filter diterapkan
53. Kosongkan field `Source` pada Filter Panel, klik `Apply` (langkah penghubung pembersih)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 1c). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: urutan sumber TC-12, TC-14, TC-15, TC-16, TC-17. Spec memakai TC-12, TC-16, TC-17, TC-15, TC-14 agar TC-14 (Search dan Filter di Tab Not Paired) berada terakhir dan tidak meninggalkan filter yang memengaruhi blok Tab All (S-09, S-10).
- Langkah penghubung (bukan dari TC, tanpa awalan `Verifikasi`, S-03): langkah 25, 34, 53 (membersihkan filter), langkah 1, 10, 18, 28, 36, 40 (amati), dan pembukaan Filter Panel. Langkah 25 hanya membersihkan filter kartu; keadaan Filter Panel sesudahnya tidak diasersi karena tidak ada Expected TC. Langkah 14, 47, dan 51 adalah anchor positif asersi universal (8b butir 2): sedikitnya satu baris tampil sebelum "hanya ...". Langkah 16 dan 24 mengasersi indikator Filter sesuai Expected c TC-16.
- Langkah 2 sampai 6 masing-masing satu kartu: nilai `of` dan `remaining` kartu yang sama dibaca dari satu kartu dan dipertahankan dalam satu `Verifikasi` per kartu (TC-12 Expected menyebut keduanya dalam satu butir per tipe).
- TC-13 (kartu `60 of 50` pada Client Over) ada di spec 017 (gate kuota), bukan di spec ini; kartu counter Tab All hanya diuji pada Client A.
- Temuan untuk QA:
  - TC-14 tidak menyebut cara membersihkan Search dan Filter sesudah blok; spec menambahkan langkah penghubung `(←)` dan kosongkan `Source` (label tombol bersih di Filter Panel tidak ditetapkan TC).
  - TC-16 butir c ("selama filter yang disetel kartu aktif") diasersi pada kedua keadaan kartu; setelah klik kartu NFC dua kali tidak ada Expected tentang indikator hilang, sehingga tidak diasersi.
  - Post Condition semua TC bernilai `-`.
- Alasan spec melewati sekitar 35 langkah (53): lima TC atas satu dataset Seed Registri A dan satu kelas harness; tiap blok berdiri sendiri (pindah tab dan pembersih filter memisahkan state), dan sebagian besar langkah adalah `Verifikasi` per nilai kartu yang tiap klausanya dapat gagal sendiri (S-01).
