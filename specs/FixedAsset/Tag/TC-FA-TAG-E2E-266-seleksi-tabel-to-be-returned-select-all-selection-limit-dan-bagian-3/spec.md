---
id: TC-FA-TAG-E2E-266-seleksi-tabel-to-be-returned-select-all-selection-limit-dan-bagian-3
title: "Seleksi Tabel To Be Returned: Checkbox Header Indeterminate dan Reset Seleksi Setelah Receive Manually Bulk (Bagian 3)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1412
  - TC-FA-TAG-1413
coverage:
  web: automated
---

# Seleksi Tabel To Be Returned: Checkbox Header Indeterminate dan Reset Seleksi Setelah Receive Manually Bulk (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned: TC-FA-TAG-1413 memakai 25 Tag dalam scope (kunci `Fixture.fixedAssetTag.tbr25`, dimuat hook `before`, tabel berisi 3 halaman pada 10 baris per halaman); TC-FA-TAG-1412 memakai tiga Tag Pre-setup: RF-00071 (RFID; Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), RF-00088 (RFID; 'Excavator 20 Ton - 5', Disposal Center, Dedi K.), dan NF-00092 (NFC; 'Laptop Pro 14 - 8', HQ Warehouse, Rina T.) (kunci `tbr3`, langkah 11). Kode dan atribut 25 Tag ditentukan seeding; TC hanya menyebut jumlahnya.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- State yang diubah: TC-FA-TAG-1412 menjalankan Receive Manually Bulk sehingga RF-00071 dan RF-00088 berstatus Damaged/Missing; hook `after` memulihkan kedua Tag ke To be Returned dan dataset ke keadaan Pre-setup empat Tag lewat fixture backend. Spec ini tidak mengubah Selection Limit.

## Test Steps

### TC-FA-TAG-1413: checkbox header memilih baris halaman aktif dan indeterminate saat sebagian dilepas

1. Klik tab `To Be Returned`
2. Centang checkbox header kolom Checkbox
3. Verifikasi sepuluh baris halaman 1 tercentang
4. Verifikasi Bulk Action Bar menampilkan "10 TAGs selected"
5. Pindah ke halaman 2
6. Verifikasi baris halaman 2 tidak tercentang
7. Kembali ke halaman 1
8. Hilangkan centang satu baris pada halaman 1
9. Verifikasi checkbox header berstatus indeterminate (ikon strip minus)
10. Verifikasi Bulk Action Bar menampilkan "9 TAGs selected"

### TC-FA-TAG-1412: Receive Manually Bulk ter-commit menutup Bulk Action Bar dan mereset seleksi

11. Atur dataset tab To Be Returned ke Pre-setup tiga Tag RF-00071, RF-00088, dan NF-00092 (kunci `tbr3`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
12. Centang RF-00071 dan RF-00088
13. Klik Bulk Action "Receive Manually"
14. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
15. Klik tombol [Submit]
16. Verifikasi dialog menutup
17. Verifikasi toast "Success, TAG has been received as damaged/missing." tampil
18. Verifikasi Bulk Action Bar tertutup
19. Verifikasi seleksi kembali 0
20. Verifikasi baris NF-00092 yang tersisa di tabel tidak tercentang

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1412 s.d. 1413). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1371 s.d. 1376 ada di spec 264; TC-FA-TAG-1408 s.d. 1411 ada di spec 265; TC-FA-TAG-1400 s.d. 1407 ada di spec 267 dan 268.
- Urutan TC di dalam spec: TC-FA-TAG-1413, lalu TC-FA-TAG-1412, karena TC-FA-TAG-1412 mengubah data (Submit) dan berada di akhir (S-10); dataset tiga Tag dimuat pada langkah penghubung 11.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 5 (memeriksa halaman 2); 7 (kembali ke halaman 1); 11 (memuat dataset 3 Tag dan membuka tab).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1412 Post Condition ("Tag RF-00071 dan RF-00088 berstatus Damaged/Missing di registri Global") tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-FA-TAG-1413 Expected a menyebut baris halaman 2 tidak tercentang tanpa langkah pindah halaman; spec menambah pindah ke halaman 2 dan kembali ke halaman 1 sebagai langkah penghubung.
  - TC-FA-TAG-1413 tidak menyebut kode Tag; spec hanya memakai jumlah 25.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
