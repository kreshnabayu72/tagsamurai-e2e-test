---
id: TC-AC-DN-E2E-122-state-preservation-navigasi-dan-sub-tab
title: "State List: Klik Ulang Menu, Pindah Sub-tab, Node Sidebar, dan Filter Bertahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-385
  - TC-AC-DN-386
  - TC-AC-DN-387
  - TC-AC-DN-604
coverage:
  web: automated
---

# State List: Klik Ulang Menu, Pindah Sub-tab, Node Sidebar, dan Filter Bertahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #14 Pohon Category (`Hardware` > `Handheld Reader` > `UHF Handheld`; `Hardware` > `Smart Fixed Reader` > `Antenna`); #15 Brand `Brand A`; #16 Device Name inti beserta SKU-nya (`Door Antenna` dan `Gate Antenna` ber-Category `Antenna`, `Gate Antenna` dan `RFID Reader` ber-Brand A); #17 seed 120 baris; #19 riwayat Changelog yang menentukan Last Modified; #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: state collapsed Category Sidebar per user dan pilihan node tidak disimpan lintas muat ulang selain yang diasersi; pilihan node dan Filter dikembalikan ke awal di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-385: Klik ulang menu Settings > Device mereset List ke default

1. Ketik Search `rfid`, tekan Enter
2. Klik header `Last Modified` (ascending)
3. Klik menu `Settings > Device` pada sidebar navigasi
4. Verifikasi kolom pencarian kosong
5. Verifikasi sort kembali default Device Name A-Z
6. Verifikasi halaman 1 menampilkan Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002

### TC-AC-DN-386: Berpindah sub-tab Device SKU lalu kembali memulihkan state List

7. Ketik Search `rfid`, tekan Enter
8. Klik header `Last Modified` dua kali (Newest First)
9. Klik sub-tab `Device SKU`
10. Klik sub-tab `Device Name`
11. Verifikasi kolom pencarian masih berisi `rfid`
12. Verifikasi sort Last Modified Newest First masih aktif
13. Verifikasi tabel menampilkan 1 baris: RFID Reader
14. Klik `(←)` pada kotak Search
15. Klik header `Last Modified` ketiga kali (netral)

### TC-AC-DN-387: Pilihan node Category Sidebar setelah F5 dan pindah sub-tab

16. Verifikasi tidak ada node yang tercentang pada Category Sidebar (baris `All Categories` tampil di atas Hardware dan TAG tanpa kotak centang)
17. Verifikasi tabel menampilkan 130 baris
18. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar, klik node `Antenna`
19. Verifikasi node `Antenna` terpilih
20. Verifikasi tabel menampilkan 2 baris: Door Antenna dan Gate Antenna
21. Klik sub-tab `Device SKU`
22. Klik sub-tab `Device Name`
23. Verifikasi node `Antenna` tetap terpilih
24. Verifikasi pohon kembali ke state expand awal
25. Verifikasi tabel tetap menampilkan 2 baris: Door Antenna dan Gate Antenna
26. Muat ulang halaman dengan F5
27. Verifikasi node `Antenna` tetap terpilih
28. Verifikasi pohon kembali ke state expand awal halaman dibuka
29. Verifikasi tabel tetap menampilkan 2 baris: Door Antenna dan Gate Antenna
30. Expand `Hardware` lalu `Smart Fixed Reader`, hapus pilihan node `Antenna`

### TC-AC-DN-604: Filter Panel yang sudah di-Apply tetap aktif setelah pindah sub-tab

31. Klik node `Hardware` pada Category Sidebar dan expand `Handheld Reader`
32. Klik ikon Filter, klik field `Brand`, centang `Brand A`, lalu klik `[Apply]`
33. Klik sub-tab `Device SKU`
34. Klik sub-tab `Device Name`
35. Verifikasi List tetap tersaring Brand `Brand A` (sedikitnya satu baris tampil dan seluruh baris ber-Brand `Brand A`)
36. Verifikasi indikator filter aktif tampil pada ikon Filter
37. Verifikasi node `Hardware` tetap aktif
38. Verifikasi node `Handheld Reader` kembali tertutup pada Sidebar
39. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
40. Hapus pilihan node `Hardware`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 14, 15, 30, 39, dan 40 mengembalikan Search, sort, pilihan node, dan Filter ke awal; langkah 3 (klik menu) sudah mereset Search dan sort untuk TC berikutnya.
- Ukuran spec (40 langkah, di atas smell 35 langkah, kode R3): satu topik (preservasi state List), satu dataset baca-saja, satu kelas harness; tiap blok TC memulai dari state yang dikembalikan ke awal sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Urutan: mengikuti sourceTc.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-387 dan TC-AC-DN-604 menyatakan pilihan node dipertahankan sementara pohon kembali ke state expand awal (Keputusan NC-17); TC-AC-DN-44 dan TC-AC-DN-45 (persistensi Sidebar) tumpang tindih sebagian dengan Expected ini.
  - TC-AC-DN-604 Expected a ("List tetap tersaring Brand `Brand A`") tidak menyebut daftar baris; spec mengasersi sifatnya tanpa daftar baris.
