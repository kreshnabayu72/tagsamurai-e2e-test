---
id: TC-GS-TAG-E2E-084-event-log-download-nama-file-dan-ekstensi
title: "Event Log: Download CSV dan XLSX per Tab (Nama File, Ekstensi, Tanpa Toast Sukses)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-257
coverage:
  web: automated
---

# Event Log: Download CSV dan XLSX per Tab (Nama File, Ekstensi, Tanpa Toast Sukses)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` tidak mengganti sesi.
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup Client A (dibaca saja): Seed Event Log `E-01` sampai `E-14` (Tab Activate TAG) dan `A-01` sampai `A-12` (Tab Audit TAG), Tabel Data Uji Dinamis TC; mekanisme seeding disediakan tim FE/BE (lihat Temuan untuk QA). Baris `E-03` (14/09/26 16:45, TAG Type RFID, Activity `Delete`, Success 3, Waiting for Approval `—`, Failed 0) dipakai sebagai baris pembaca isi berkas Tab Activate TAG; baris itu dicari di berkas lewat Date `14/09/26 16:45`.
- Event Log menumpuk antar spec, sehingga isi berkas tidak diasersi sebagai jumlah baris absolut; asersi isi memakai baris seed `E-03`.
- Kemampuan teknis (disediakan tim FE): pembaca berkas CSV/XLSX terunduh (nama berkas dan isi sel); pengamat toast.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-TAG-257: Download Event Log, nama file per tab dan ekstensi mengikuti pilihan

1. Klik tombol `Event Log` di toolbar
2. Pada Tab Activate TAG, klik `Download`, lalu pilih `Download as CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas `Tag-Activate-Log.csv` terunduh
5. Verifikasi kolom Waiting for Approval pada baris Date `14/09/26 16:45` di berkas CSV bernilai `-` (nilai `—` diexport `-`)
6. Pada Tab Activate TAG, klik `Download`, lalu pilih `Download as XLSX`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas `Tag-Activate-Log.xlsx` terunduh
9. Verifikasi kolom Waiting for Approval pada baris Date `14/09/26 16:45` di berkas XLSX bernilai `-`
10. Klik tab `Audit TAG`
11. Klik `Download`, lalu pilih `Download as CSV`
12. Verifikasi tidak ada toast sukses
13. Verifikasi berkas `Tag-Audit-Log.csv` terunduh
14. Klik `Download`, lalu pilih `Download as XLSX`
15. Verifikasi tidak ada toast sukses
16. Verifikasi berkas `Tag-Audit-Log.xlsx` terunduh

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas f (binary buffer): isi berkas CSV/XLSX dibaca; kegagalan ekspor tidak ada dalam spec ini.
- Absence toast (langkah 3, 7, 12, 15) diletakkan segera setelah pemicu dan sebelum asersi artefak (bagian 8b butir 11); pemicu (klik pilihan format) menjadi anchor positif dan buktinya menyusul pada `Verifikasi` berkas terunduh.
- Langkah 5 dan 9 mengasersi Expected b TC-257 ("kolom Waiting for Approval nilai `—` diexport `-`") pada baris seed `E-03`, satu-satunya baris Delete yang nilainya `—` pada Data Uji dan tidak berubah oleh spec lain.
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Seed Event Log tidak didefinisikan di TC (Q-4).
  - TC-257 hanya menyebut nilai export `-` untuk Waiting for Approval Tab Activate TAG; isi sel lain dan isi berkas Tab Audit TAG tidak diasersi karena Expected tidak menyebutnya.
  - TC-257 tidak menyebut apakah Download mengikuti Search dan Filter yang aktif; spec mengunduh tanpa Search dan Filter.
